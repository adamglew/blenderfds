import_from_fds_tree(
    test=test,
    path="/opt/FDS/FDS6/Validation/",
    compare_with_ref=False,
    run_fds = False,
    exclude_files = None,
    exclude_dirs=("Crown_fires", "Askervein_Hill"),
)


# Exclusions:
# Crown_fires are huge
# Askervein_hills have bingeom in another repository
