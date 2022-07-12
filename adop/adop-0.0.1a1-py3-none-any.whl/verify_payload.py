def verify_content(header_content_len: int, received_data_len: int, file_len: int):
    """
    Make sure that received data length matches request content length.
    """

    yield "verify data"
    if file_len != received_data_len:
        raise ValueError(
            f"file_len {file_len} and received_data_len {received_data_len} differs"
        )
    if file_len != header_content_len:
        raise ValueError(
            f"file_len {file_len} and Content-Length {header_content_len} differs"
        )


def verify_root(root_dir_name: str, headers: dict):
    yield "verify root dir"
    root_from_header = headers.get("Root", "")
    if not (root_dir_name.lower() == root_from_header.lower()):
        raise ValueError(
            f" zip root dir: {root_dir_name} and header Root: {root_from_header} differs"
        )
