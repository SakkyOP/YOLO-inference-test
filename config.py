class Options:
    # add other options as you please but name is required
    # the additional options are for running evaluation in model.py
    def __init__(self, name):
        self.name = name
        
options = Options('yolov8n')
## ==== Optional Args ====
# options.src # Source, could be img, array, video, etc.
# options.conf # Confidence score threshold
# options.size # img size affects model speed
# options.show # display the resulting predicitons annotated on the image
# options.crop # save the cropped parts where objects were detected
# options.save # save the annotated image / video