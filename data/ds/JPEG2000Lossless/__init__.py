"""1.2.840.10008.1.2.4.90 - JPEG 2000 Image Compression (Lossless Only)"""

INDEX = {
    '693_J2KR.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 512),
        'Columns' : ('US', 512),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 1),
        'WindowCenter' : ('DS', '40'),
        'WindowWidth' : ('DS', '100'),
        'RescaleIntercept' : ('DS', '-1024'),
        'RescaleSlope' : ('DS', '1'),
    },
    '966.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 2128),
        'Columns' : ('US', 2000),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '2048'),
        'WindowWidth' : ('DS', '4096'),
        'RescaleIntercept' : ('DS', '0'),
        'RescaleSlope' : ('DS', '1'),
        'Status' : ('US', 0xC000),
        'ImageComments' : ('LT', 'Invalid COM marker at offset 4099003'),
        'RetrieveURI' : ('UR', 'https://github.com/pydicom/pydicom/issues/966'),
    },
    '966_fixed.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 2128),
        'Columns' : ('US', 2000),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '2048'),
        'WindowWidth' : ('DS', '4096'),
        'RescaleIntercept' : ('DS', '0'),
        'RescaleSlope' : ('DS', '1'),
        'Status' : ('US', 0x0000),
        'ImageComments' : ('LT', 'Version of 966.dcm without bad COM marker'),
        'RetrieveURI' : ('UR', 'https://github.com/pydicom/pydicom/issues/966'),
    },
    'emri_small_jpeg_2k_lossless.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '10'),
        'Rows' : ('US', 64),
        'Columns' : ('US', 64),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
    },
    'explicit_VR-UN.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 512),
        'Columns' : ('US', 512),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 1),
        'RescaleIntercept' : ('UN', 0x3020),
        'RescaleSlope' : ('UN', 0x3120),
    },
    'JPEG2KLossless_1s_1f_u_16_16.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1416),
        'Columns' : ('US', 1420),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '2725'),
        'WindowWidth' : ('DS', '5310'),
        'RescaleIntercept' : ('DS', '0'),
        'RescaleSlope' : ('DS', '1'),
    },
    'MR2_J2KR.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1024),
        'Columns' : ('US', 1024),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '1000'),
        'WindowWidth' : ('DS', '2000'),
        'RescaleIntercept' : ('DS', '0.000061'),
        'RescaleSlope' : ('DS', '3.774114'),
    },
    'MR_small_jp2klossless.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 64),
        'Columns' : ('US', 64),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 1),
        'WindowCenter' : ('DS', '600'),
        'WindowWidth' : ('DS', '1600'),
    },
    'RG1_J2KR.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1955),
        'Columns' : ('US', 1841),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 15),
        'HighBit' : ('US', 14),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '15000'),
        'WindowWidth' : ('DS', '30000'),
    },
    'RG3_J2KR.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1760),
        'Columns' : ('US', 1760),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 10),
        'HighBit' : ('US', 9),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '550'),
        'WindowWidth' : ('DS', '1024'),
    },
    'US1_J2KR.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.90'),
        'SamplesPerPixel' : ('US', 3),
        'PhotometricInterpretation' : ('CS', 'YBR_RCT'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 480),
        'Columns' : ('US', 640),
        'BitsAllocated' : ('US', 8),
        'BitsStored' : ('US', 8),
        'HighBit' : ('US', 7),
        'PixelRepresentation' : ('US', 0),
    },
}
