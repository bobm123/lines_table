=====
Usage
=====

To use Lines Table in a project::

    >>> from lines_table.lines_table import offset_reader, rake_angle
    >>> offsets = offset_reader('test_data/Cartopper.csv')
    >>> print(offsets)

Once the data has been imported a rake angle can be applied at any station (usually the bow or stern) of the hull. If the offset data contains a set of angles they can be applied as follows

    >>> if 'angle' in offsets:
    >>>     for i,angle in enumerate(offsets['angle']):
    >>>         offset_data = rake_angle(offset_data, i, 90 - angle)

In other cases, the angles may be given in supplemental text, a side view of the boat, or as a note. In these cases the angles can be applied individually.

    >>> angle = 17  # measured from plan view 
    >>> offset_data = rake_angle(offset_data, 0, 90 - angle)
