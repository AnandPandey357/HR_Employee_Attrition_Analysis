"""
HR Employee Attrition Analysis - Data Preprocessing Script
This script handles data cleaning, preprocessing, and preparation for analysis.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
import json

class DataPreprocessor:
    """Handle all data preprocessing operations"""
    
    def __init__(self, input_path, output_dir):
        self.input_path = input_path
        self.output_dir = output_dir
        self.df = None
        self.label_encoders = {}
        self.scaler = StandardScaler()
        
    def load_data(self):
        """Load the raw dataset"""
        print("Loading dataset...")
        self.df = pd.read_csv(self.input_path)
        print(f"Dataset loaded with {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        return self.df
    
    def check_missing_values(self):
        """Check for missing values in the dataset"""
        print("\n=== Missing Values Analysis ===")
        missing = self.df.isnull().sum()
        print(missing)
        if missing.sum() == 0:
            print("No missing values found in the dataset.")
        return missing
    
    def handle_missing_values(self):
        """Handle missing values with appropriate strategies"""
        print("\n=== Handling Missing Values ===")
        # For numerical columns, fill with median
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if self.df[col].isnull().sum() > 0:
                median_val = self.df[col].median()
                self.df[col].fillna(median_val, inplace=True)
                print(f"Filled missing values in {col} with median: {median_val}")
        
        # For categorical columns, fill with mode
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if self.df[col].isnull().sum() > 0:
                mode_val = self.df[col].mode()[0]
                self.df[col].fillna(mode_val, inplace=True)
                print(f"Filled missing values in {col} with mode: {mode_val}")
        
        return self.df
    
    def remove_duplicates(self):
        """Remove duplicate records"""
        print("\n=== Removing Duplicates ===")
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates()
        final_count = len(self.df)
        removed = initial_count - final_count
        print(f"Removed {removed} duplicate records")
        return self.df
    
    def encode_categorical_variables(self):
        """Encode categorical variables using Label Encoding"""
        print("\n=== Encoding Categorical Variables ===")
        categorical_cols = ['Gender', 'Department', 'JobRole', 'Overtime', 'Attrition']
        
        for col in categorical_cols:
            if col in self.df.columns:
                le = LabelEncoder()
                self.df[col + '_Encoded'] = le.fit_transform(self.df[col])
                self.label_encoders[col] = le
                print(f"Encoded {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")
        
        # Save encoding mappings for reference
        encoding_mapping = {}
        for col, le in self.label_encoders.items():
            encoding_mapping[col] = {str(k): int(v) for k, v in zip(le.classes_, le.transform(le.classes_))}
        
        with open(os.path.join(self.output_dir, 'encoding_mapping.json'), 'w') as f:
            json.dump(encoding_mapping, f, indent=2)
        
        return self.df
    
    def normalize_numerical_features(self):
        """Normalize numerical features using StandardScaler"""
        print("\n=== Normalizing Numerical Features ===")
        numerical_cols = ['Age', 'MonthlyIncome', 'JobSatisfaction', 'WorkLifeBalance']
        
        # Store original values for reference
        original_values = self.df[numerical_cols].copy()
        
        # Apply normalization
        self.df[numerical_cols] = self.scaler.fit_transform(self.df[numerical_cols])
        
        print(f"Normalized {len(numerical_cols)} numerical features")
        print("Normalization parameters (mean, std):")
        for i, col in enumerate(numerical_cols):
            print(f"{col}: mean={self.scaler.mean_[i]:.2f}, std={self.scaler.scale_[i]:.2f}")
        
        return self.df
    
    def create_derived_features(self):
        """Create derived features for analysis"""
        print("\n=== Creating Derived Features ===")
        
        # Income categories
        self.df['IncomeCategory'] = pd.cut(
            self.df['MonthlyIncome'], 
            bins=[0, 4000, 6000, 8000, float('inf')],
            labels=['Low', 'Medium', 'High', 'Very High']
        )
        
        # Age groups
        self.df['AgeGroup'] = pd.cut(
            self.df['Age'],
            bins=[0, 30, 40, 50, float('inf')],
            labels=['20-30', '31-40', '41-50', '50+']
        )
        
        # Satisfaction score (combined)
        self.df['OverallSatisfaction'] = (
            self.df['JobSatisfaction'] + self.df['WorkLifeBalance']
        ) / 2
        
        print("Created derived features: IncomeCategory, AgeGroup, OverallSatisfaction")
        
        return self.df
    
    def save_processed_data(self):
        """Save processed data to CSV"""
        print("\n=== Saving Processed Data ===")
        output_path = os.path.join(self.output_dir, 'hr_employee_data_processed.csv')
        self.df.to_csv(output_path, index=False)
        print(f"Processed data saved to: {output_path}")
        
        # Also save a summary
        summary = {
            'total_records': len(self.df),
            'columns': list(self.df.columns),
            'missing_values': self.df.isnull().sum().to_dict(),
            'data_types': self.df.dtypes.astype(str).to_dict()
        }
        
        summary_path = os.path.join(self.output_dir, 'data_summary.json')
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"Data summary saved to: {summary_path}")
        
        return self.df
    
    def generate_preprocessing_report(self):
        """Generate a preprocessing report"""
        print("\n=== Preprocessing Report ===")
        report = {
            'original_rows': len(pd.read_csv(self.input_path)),
            'processed_rows': len(self.df),
            'columns_before': len(pd.read_csv(self.input_path).columns),
            'columns_after': len(self.df.columns),
            'duplicates_removed': len(pd.read_csv(self.input_path)) - len(self.df),
            'categorical_encoded': list(self.label_encoders.keys()),
            'numerical_normalized': ['Age', 'MonthlyIncome', 'JobSatisfaction', 'WorkLifeBalance'],
            'derived_features': ['IncomeCategory', 'AgeGroup', 'OverallSatisfaction']
        }
        
        report_path = os.path.join(self.output_dir, 'preprocessing_report.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\nPreprocessing Summary:")
        print(f"- Original records: {report['original_rows']}")
        print(f"- Processed records: {report['processed_rows']}")
        print(f"- Duplicates removed: {report['duplicates_removed']}")
        print(f"- Categorical variables encoded: {len(report['categorical_encoded'])}")
        print(f"- Numerical features normalized: {len(report['numerical_normalized'])}")
        print(f"- Derived features created: {len(report['derived_features'])}")
        
        return report
    
    def run_full_preprocessing(self):
        """Run the complete preprocessing pipeline"""
        print("=" * 60)
        print("HR EMPLOYEE ATTRITION DATA PREPROCESSING")
        print("=" * 60)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Check missing values
        self.check_missing_values()
        
        # Step 3: Handle missing values
        self.handle_missing_values()
        
        # Step 4: Remove duplicates
        self.remove_duplicates()
        
        # Step 5: Encode categorical variables
        self.encode_categorical_variables()
        
        # Step 6: Normalize numerical features
        self.normalize_numerical_features()
        
        # Step 7: Create derived features
        self.create_derived_features()
        
        # Step 8: Save processed data
        self.save_processed_data()
        
        # Step 9: Generate report
        report = self.generate_preprocessing_report()
        
        print("\n" + "=" * 60)
        print("PREPROCESSING COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
        return self.df, report


def main():
    """Main execution function"""
    # Define paths
    input_path = '../data/raw/hr_employee_data.csv'
    output_dir = '../data/processed'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize preprocessor
    preprocessor = DataPreprocessor(input_path, output_dir)
    
    # Run preprocessing
    processed_df, report = preprocessor.run_full_preprocessing()
    
    print("\n✓ Data preprocessing completed successfully!")
    print(f"✓ Improved data accuracy by handling missing values and duplicates")
    print(f"✓ Prepared {len(processed_df)} records for analysis")


if __name__ == "__main__":
    main()
