import csv
import math

file_name = input("Enter CSV file name: ")

genes = []

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        gene = row["Gene"]

        control = [
            float(row["Control1"]),
            float(row["Control2"])
        ]

        treatment = [
            float(row["Treatment1"]),
            float(row["Treatment2"])
        ]

        avg_control = sum(control) / len(control)
        avg_treatment = sum(treatment) / len(treatment)

        # Avoid division by zero
        if avg_control == 0:
            fold_change = 0
            log2fc = 0
        else:
            fold_change = avg_treatment / avg_control
            log2fc = math.log2(fold_change)

        # Simple threshold for this lab
        if log2fc >= 1:
            status = "Upregulated"
        elif log2fc <= -1:
            status = "Downregulated"
        else:
            status = "Not Significant"

        genes.append([
            gene,
            avg_control,
            avg_treatment,
            fold_change,
            log2fc,
            status
        ])

print("\nRNA-Seq Differential Gene Expression Analysis")
print("-" * 75)

print(
    f"{'Gene':<10}"
    f"{'Control':<12}"
    f"{'Treatment':<12}"
    f"{'Fold Change':<14}"
    f"{'Log2FC':<10}"
    f"{'Status'}"
)

print("-" * 75)

for gene in genes:
    print(
        f"{gene[0]:<10}"
        f"{gene[1]:<12.2f}"
        f"{gene[2]:<12.2f}"
        f"{gene[3]:<14.2f}"
        f"{gene[4]:<10.2f}"
        f"{gene[5]}"
    )

print("\nSummary:")
print("Upregulated genes:",
      sum(1 for gene in genes if gene[5] == "Upregulated"))

print("Downregulated genes:",
      sum(1 for gene in genes if gene[5] == "Downregulated"))

print("Not significant:",
      sum(1 for gene in genes if gene[5] == "Not Significant"))