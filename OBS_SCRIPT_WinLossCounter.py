import obspython as obs
import math, time, json

dataFile = open('D:\Python\OBS Win Loss Counter\Data.obspt','r') 
j = json.load(dataFile)


def script_description():
    
    
    d = j['description']['text']
    return d

def script_tick(seconds): #adding: a process to update the text in the Win loss counter

    #dataFile = open('D:\Python\OBS Win Loss Counter\Data.obspt','r') 
    dataFile.seek(0,0)
    j = json.load(dataFile)


    current_scene_as_source = obs.obs_frontend_get_current_scene()
    if current_scene_as_source:
        current_scene = obs.obs_scene_from_source(current_scene_as_source)
        scene_item = obs.obs_scene_find_source_recursive(current_scene, "Win_Loss_Counter")
        if scene_item:#changes text
            w = j['Counter']['Wins']
            l = j['Counter']['Losses']
            d = j['Counter']['Draws']
            #print(w+ " "+l+" "+d)
            txt = "W:"+w+ " L:"+l+" D:"+d
            #get text source settings
            #get properties
            #find text property
            #change text property
            #update_properties(source)
            source = obs.obs_get_source_by_name("Win_Loss_Counter")
            settings = obs.obs_data_create()
            obs.obs_data_set_string(settings, "text", txt)
            obs.obs_source_update(source, settings)
            obs.obs_data_release(settings)
            obs.obs_source_release(source)
            obs.obs_scene_release(current_scene)
          
            


    current_scene_as_source = obs.obs_frontend_get_current_scene()
    if current_scene_as_source:
        current_scene = obs.obs_scene_from_source(current_scene_as_source)
        scene_item = obs.obs_scene_find_source_recursive(current_scene, "Ratings")
        if scene_item:#changes text
            s = j['Ratings']['Start']
            c = j['Ratings']['Current']
           
            #print(w+ " "+l+" "+d)
            txt = "Start:"+s+ " Current:"+c
            #get text source settings
            #get properties
            #find text property
            #change text property
            #update_properties(source)
            source = obs.obs_get_source_by_name("Ratings")
            settings = obs.obs_data_create()
            obs.obs_data_set_string(settings, "text", txt)
            obs.obs_source_update(source, settings)
            obs.obs_data_release(settings)
            obs.obs_source_release(source)
            obs.obs_scene_release(current_scene)
        
            






 

