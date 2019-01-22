import wx


def resize_bitmap(b: wx.Bitmap, width, height) -> wx.Bitmap:
    """resize bitmap so as to fit in specified width and height so as not to
    exceed the original size.
    """
    # @todo enable to choice Correct the orientation of the image
    i: wx.Image = b.ConvertToImage()
    s: wx.Size = i.GetSize()
    old_w = s.GetWidth()
    old_h = s.GetHeight()

    if old_w <= width and old_h <= height:
        new_w = width
        new_h = height
    else:
        if old_w > width:
            new_w = width
            new_h = (old_h * width) / old_w
        elif old_h > height:
            new_w = (old_w * height) / old_h
            new_h = height
        # Re-correction if overflowing after correction
        if new_w > width:
            new_w = width
            new_h = (old_h * width) / old_w
        elif new_h > height:
            new_w = (old_w * height) / old_h
            new_h = height

    i = i.Scale(int(new_w), int(new_h), wx.IMAGE_QUALITY_HIGH)
    return wx.Bitmap(i)