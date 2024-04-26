from ultralytics import YOLO, NAS, RTDETR, FastSAM
from config import options

model= YOLO(options.name+'.pt')

if __name__ == '__main__':
    # results = model.predict(
    #                             source=options.src,
    #                             conf=options.conf,
    #                             imgsz=options.size,
    #                             show=options.show,
    #                             save_crop=options.crop,
    #                             save=options.save
    #                         )
    
    model.export()