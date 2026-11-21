import matplotlib.pyplot as plt

# Plot 1: SNP vs Indel counts
categories = ['SNPs', 'Indels']
counts = [54447, 389]

plt.figure(figsize=(6,4))
plt.bar(categories, counts, color=['steelblue', 'coral'])
plt.title('Variant Type Distribution')
plt.ylabel('Count')
for i, v in enumerate(counts):
    plt.text(i, v + 500, str(v), ha='center')
plt.tight_layout()
plt.savefig('variant_type_distribution.png', dpi=150)
plt.close()

# Plot 2: Quality score distribution
import subprocess
result = subprocess.run(
    "bcftools view -H called_variants.vcf | cut -f6",
    shell=True, capture_output=True, text=True
)
quals = [float(x) for x in result.stdout.strip().split('\n') if x]

plt.figure(figsize=(6,4))
plt.hist(quals, bins=50, color='seagreen')
plt.yscale('log')
plt.title('Variant Quality Score Distribution')
plt.xlabel('QUAL score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('quality_distribution.png', dpi=150)
plt.close()

print("Both plots saved successfully!")

