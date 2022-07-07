try:
    import sarus.pandas_profiling.profile_report
except NameError:
    print("pandas_profiling not found, ProfileReport not available.")
