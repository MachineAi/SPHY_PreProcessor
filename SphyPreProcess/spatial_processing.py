import os

#-Class with gdal processing commands
class SpatialProcessing():
    def __init__(self, infile, outfile, s_srs, t_srs, resolution, resampling='bilinear', rtype='Float32', extra=None, projwin=None):
        self.input = infile
        self.output = outfile
        self.s_srs = s_srs
        self.t_srs = t_srs
        self.t_res = str(resolution)
        self.resampling = resampling
        self.rtype = rtype
        self.extra = extra
        self.projwin = projwin
        
    #-Reproject, resample, and clip to extent
    def reproject(self):
        command = 'gdalwarp -s_srs ' + self.s_srs + ' -t_srs ' + self.t_srs + ' -r ' + self.resampling\
                        + ' -tr ' + self.t_res + ' ' + self.t_res +' -ot ' + self.rtype + ' ' + self.extra\
                        + ' ' + self.input + ' ' + self.output 
        return command
    
    #-Convert raster format
    def rasterTranslate(self):
        command = 'gdal_translate ' + self.extra + ' ' + self.input + ' ' + self.output
        return command
    
    #-Rasterize Vector
    def rasterize(self):
        d = os.path.dirname(self.input)
        fi = os.path.relpath(self.input, d)
        layer = fi.split('.shp')[0]
        command = 'gdal_rasterize ' + self.extra + ' -l ' + layer + ' -tr ' + self.t_res + ' ' + \
            self.t_res + ' ' + self.input + ' ' + self.output
        return command
    
