# NGS Variant Calling Pipeline — E. coli Whole Genome Sequencing

## Overview
End-to-end NGS pipeline for detecting and interpreting genomic variants in *Escherichia coli* (K-12 MG1655 reference strain), using publicly available Illumina paired-end sequencing data from NCBI SRA.

**Pipeline:** Raw reads → QC → Trimming → Alignment → Variant Calling → Filtering → Biological Interpretation

## Data Source
- **Accession:** SRR40689140 (NCBI SRA)
- **Study:** Whole-genome sequencing of pathogenic bacterial species, LA County Public Health Lab (PRJNA1004324)
- **Reads:** 455,404 paired-end Illumina MiSeq reads (113.2 Mbp)
- **Reference genome:** *E. coli* K-12 MG1655 (GCF_000005845.2)

## Tools Used
| Step | Tool |
|---|---|
| Quality Control | FastQC |
| Trimming | fastp |
| Alignment | BWA-MEM |
| Sort/Index | Samtools |
| Variant Calling | BCFtools |
| Statistics | bcftools stats |
| Visualization | Python (matplotlib) |
| Gene Annotation | Manual GFF cross-referencing (NCBI) |

## Pipeline Steps

1. **Data acquisition** — Downloaded via `prefetch` + `fasterq-dump`
2. **Quality control** — FastQC confirmed good read quality (scores 32-40, well above threshold)
3. **Trimming** — fastp removed low-quality bases and adapter contamination
4. **Alignment** — BWA-MEM aligned trimmed reads to reference genome
5. **Sort/Index** — Samtools produced sorted, indexed BAM file
6. **Variant calling** — BCFtools identified 54,836 total variants
7. **Filtering** — Filtered to 39,656 high-confidence variants (QUAL>200, DP>30)
8. **Statistics** — Generated summary statistics (see Results)
9. **Biological interpretation** — Manually cross-referenced top 10 highest-quality variants against NCBI's GFF annotation

## Results

**Variant Summary:**
- Total variants: 54,836
- SNPs: 54,447
- Indels: 389
- Ts/Tv ratio: 2.54 (consistent with real biological signal, not sequencing noise)
- High-confidence variants (QUAL>200, DP>30): 39,656

**Quality distribution:** The majority of raw variant calls clustered near maximum quality (~225-228), with a smaller tail of lower-confidence calls (down to ~3), justifying the QUAL>200 filtering threshold applied for downstream analysis.

**Gene-level findings:** Of the 10 highest-confidence variants, 4 fell within annotated genes, including a functional non-coding RNA gene (*rygC*) and three protein-coding genes. The remainder were located in intergenic regions.

## A Note on Methodology
Automated annotation via SnpEff was attempted but the required database download was blocked at the network level (confirmed via multiple browsers and mobile hotspot testing). As a workaround, gene-level annotation was performed manually using NCBI's GFF annotation file for the reference genome, cross-referenced against variant genomic coordinates using command-line tools (awk).

## Files
- `called_variants.vcf` — Full variant call set
- `high_confidence_variants.vcf` — Filtered high-confidence variants
- `variant_stats.txt` — Summary statistics
- `variant_type_distribution.png` — SNP vs. Indel visualization
- `top10_variants.txt` — Highest-quality variants with gene annotations

## Title
**Author:** Vaishnavi Sharma

