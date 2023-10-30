def relative_from_root(path: str):
    import qa_guru_python_07_22
    from pathlib import Path

    return (
        Path(qa_guru_python_07_22.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
