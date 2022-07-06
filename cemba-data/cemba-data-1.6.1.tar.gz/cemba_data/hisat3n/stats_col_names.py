# "DELETE" means this column will be removed from the output file
# "" means the name will not be changed
# "CertainMetricNames" means the name will be changed to "CertainMetricNames"


COL_NAMES = {
    ('cell_parser_cutadapt_trim_stats', 'status'): 'DELETE',
    ('cell_parser_cutadapt_trim_stats', 'in_reads'): 'InputReadPairs',
    ('cell_parser_cutadapt_trim_stats', 'in_bp'): 'InputReadPairsBP',
    ('cell_parser_cutadapt_trim_stats', 'too_short'): 'DELETE',
    ('cell_parser_cutadapt_trim_stats', 'too_long'): 'DELETE',
    ('cell_parser_cutadapt_trim_stats', 'too_many_n'): 'DELETE',
    ('cell_parser_cutadapt_trim_stats', 'out_reads'): 'TrimmedReadPairs',
    ('cell_parser_cutadapt_trim_stats', 'w/adapters'): 'R1WithAdapters',
    ('cell_parser_cutadapt_trim_stats', 'qualtrim_bp'): 'R1QualTrimBP',
    ('cell_parser_cutadapt_trim_stats', 'out_bp'): 'R1TrimmedReadsBP',
    ('cell_parser_cutadapt_trim_stats', 'w/adapters2'): 'R2WithAdapters',
    ('cell_parser_cutadapt_trim_stats', 'qualtrim2_bp'): 'R2QualTrimBP',
    ('cell_parser_cutadapt_trim_stats', 'out2_bp'): 'R2TrimmedReadsBP',
    ('cell_parser_hisat_summary', 'ReadPairsMappedInPE'): 'DELETE',
    ('cell_parser_hisat_summary', 'PEUnmappableReadPairs'): 'DELETE',
    ('cell_parser_hisat_summary', 'PEUniqueMappedReadPairs'): 'DELETE',
    ('cell_parser_hisat_summary', 'PEMultiMappedReadPairs'): 'DELETE',
    ('cell_parser_hisat_summary', 'PEDiscordantlyUniqueMappedReadPairs'): 'DELETE',
    ('cell_parser_hisat_summary', 'ReadsMappedInSE'): 'DELETE',
    ('cell_parser_hisat_summary', 'SEUnmappableReads'): 'DELETE',
    ('cell_parser_hisat_summary', 'SEUniqueMappedReads'): 'DELETE',
    ('cell_parser_hisat_summary', 'SEMultiMappedReads'): 'DELETE',
    ('cell_parser_hisat_summary', 'UniqueMappedReads'): 'UniqueMappedReads',
    ('cell_parser_hisat_summary', 'MultiMappedReads'): 'MultiMappedReads',
    ('cell_parser_hisat_summary', 'UniqueMappingRate'): 'UniqueMappingRate',
    ('cell_parser_hisat_summary', 'MultiMappingRate'): 'MultiMappingRate',
    ('cell_parser_hisat_summary', 'OverallMappingRate'): 'OverallMappingRate',
    ('cell_parser_picard_dedup_stat', 'LIBRARY'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'UNPAIRED_READS_EXAMINED'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'READ_PAIRS_EXAMINED'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'SECONDARY_OR_SUPPLEMENTARY_RDS'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'UNMAPPED_READS'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'UNPAIRED_READ_DUPLICATES'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'READ_PAIR_DUPLICATES'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'READ_PAIR_OPTICAL_DUPLICATES'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'PERCENT_DUPLICATION'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'ESTIMATED_LIBRARY_SIZE'): 'DELETE',
    ('cell_parser_picard_dedup_stat', 'FinalReads'): '',
    ('cell_parser_picard_dedup_stat', 'DuplicatedReads'): '',
    ('cell_parser_picard_dedup_stat', 'PCRDuplicationRate'): '',
    ('cell_parser_feature_count_summary', 'Assigned'): 'AssignedRNAReads',
    ('cell_parser_feature_count_summary', 'Unassigned_Unmapped'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Read_Type'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Singleton'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_MappingQuality'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Chimera'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_FragmentLength'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Duplicate'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_MultiMapping'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Secondary'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_NonSplit'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_NoFeatures'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Overlapping_Length'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Ambiguity'): 'DELETE',
    ('cell_parser_feature_count_summary', 'Unassigned_Total'): 'UnassignedRNAReads',
    ('cell_parser_feature_count_summary', 'AssignedRNAReadsRate'): 'AssignedRNAReadsRate',
}
