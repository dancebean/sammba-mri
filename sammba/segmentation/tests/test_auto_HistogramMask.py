# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..interfaces import HistogramMask


def test_HistogramMask_inputs():
    input_map = dict(closing=dict(usedefault=True,
    ),
    connected=dict(usedefault=True,
    ),
    dilation_size=dict(usedefault=True,
    ),
    in_file=dict(mandatory=True,
    ),
    intensity_threshold=dict(),
    lower_cutoff=dict(usedefault=True,
    ),
    opening=dict(usedefault=True,
    ),
    out_file=dict(keep_extension=True,
    name_source='in_file',
    name_template='%s_histo_mask',
    ),
    upper_cutoff=dict(usedefault=True,
    ),
    verbose=dict(usedefault=True,
    ),
    volume_threshold=dict(usedefault=True,
    ),
    )
    inputs = HistogramMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_HistogramMask_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = HistogramMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
