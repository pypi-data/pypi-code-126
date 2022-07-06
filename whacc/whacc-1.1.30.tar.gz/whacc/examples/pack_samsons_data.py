import matplotlib.pyplot as plt
from tqdm.auto import tqdm
from imgaug import augmenters as iaa  # optional program to further augment data

from whacc import utils
import numpy as np
from whacc import image_tools
from natsort import natsorted, ns
import pickle
import pandas as pd
import os
import copy
import seaborn as sns
from keras.preprocessing.image import ImageDataGenerator
import h5py

from whacc import utils
import h5py
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


bd_fileLists = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/fileLists/'
bd_binarizedContacts_All = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/binarizedContacts_All/'
save_dir = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/dictionary_saves/'
utils.make_path(save_dir)

final_dict = dict()
bd_fileLists = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/fileLists'
f_list = utils.sort(utils.get_files(bd_fileLists, '*.mat'))
for f in tqdm(f_list):
    d = dict()
    tmp1 = utils.loadmat(f)
    fileList = tmp1['fileList']
    d['file_list'] = fileList
    add_name = os.path.basename(f).split('_fileList.mat')[0]
    contact_dir = bd_binarizedContacts_All + add_name
    all_contacts = []
    frame_nums = []
    contact_names = utils.sort(utils.get_files(contact_dir, '*.mat'))
    d['contact_names'] = contact_names

    for k in contact_names:
        tmp2 = utils.loadmat(k)['binarizedContacts']
        frame_nums.append(len(tmp2))
        all_contacts.append(tmp2)
    d['contacts'] = all_contacts
    d['frame_nums'] = frame_nums

    save_name = save_dir + add_name + '.pkl'
    utils.save_obj(d, save_name)
    final_dict[add_name] = d


save_name = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/final_dict.pkl'
utils.save_obj(final_dict, save_name)


final_dict = T_V_Test_dict = utils.load_obj(save_name)
utils.info(final_dict['Session1'])

def smooth(y, box_pts):#$%
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def h5_to_dict(h5_in):
    d = dict()
    with h5py.File(h5_in, 'r') as h:
        for k in h.keys():
            d[k] = h[k][:]
    return d

T_V_Test_dict = [{'file_list':[], 'contact_names':[], 'contacts':[], 'frame_nums':[], 'session':[], 'session_index':[],
                  '80_border_inds':[], '20_border_inds':[], '10_border_inds':[], '3_border_inds':[]}]*3

for k in final_dict.keys():
    L = len(final_dict[k]['frame_nums'])
    np.random.seed(0)
    T_V_Test_inds = utils.split_list_inds(range(L), [6, 2, 2])
    final_dict[k]['T_V_Test_inds'] = T_V_Test_inds
    for ind1, kk in enumerate(T_V_Test_inds):
        T_V_Test_dict[ind1]
        for i in kk:
            T_V_Test_dict[ind1]['session_index'].append(i)
            T_V_Test_dict[ind1]['session'].append(k)
            T_V_Test_dict[ind1]['file_list'].append(final_dict[k]['file_list'][i])
            T_V_Test_dict[ind1]['contact_names'].append(final_dict[k]['contact_names'][i])
            T_V_Test_dict[ind1]['frame_nums'].append(final_dict[k]['frame_nums'][i])
            T_V_Test_dict[ind1]['contacts'].append(final_dict[k]['contacts'][i])
            for border_tmp in [80, 20, 10, 3]:
                border = border_tmp*2+1
                tmp2 = smooth(T_V_Test_dict[ind1]['contacts'][-1], border)
                good_inds = tmp2>0
                T_V_Test_dict[ind1][str(border_tmp) +'_border_inds'].append(good_inds)
save_name = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/final_T_V_Test_dict.pkl'
utils.save_obj(T_V_Test_dict, save_name)

T_V_Test_dict = utils.load_obj(save_name)

utils.info(T_V_Test_dict[0])

utils.info(T_V_Test_dict[0]['session'])

final_dict['Session1']['file_list'][:4]


h5_bd_session = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/'
# fn = []
for set_dict in T_V_Test_dict: # list of dicts each with all info needed to make sets
    # from set_dict I need the session and the video number that matches
    for sess in np.unique(set_dict['session']): # ook through all the session
        h5_list = utils.sort(utils.get_h5s(h5_bd_session + sess)) # get list of h5s per each session
        each_h5_inds = [int(os.path.basename(k).split('-')[-1][:-4]) for k in set_dict['file_list'][:]]
        sess_inds = np.asarray(set_dict['session'][:]) == sess
        for h5 in h5_list: # for now just session 1 TEMP
            with h5py.File(h5, 'r') as h:
                full_file_names = [n.decode("ascii", "ignore") for n in h['full_file_names'][:]]
                file_name_nums = h['file_name_nums'][:]
                np.unique(file_name_nums)


                final_features_2105 = h['final_features_2105'][:]

                print(h.keys())
                fn = h['frame_nums'][:]
                asdf


h = h5_to_dict(h5)
utils.info(h)
full_file_names = [n.decode("ascii", "ignore") for n in h['full_file_names'][:]]

utils.info(set_dict)


set_dict['file_list'][-1]
set_dict['contact_names'][-1]

all_features = []
for h5 in tqdm(h5_list):
    with h5py.File(h5, 'r') as h:
        all_features.append(h['final_features_2105'][:])




def combine_final_h5s(h5_file_list_to_combine, delete_extra_files=False):
    fn = h5_file_list_to_combine[0].split('final')[0] + 'final_combined.h5'
    h5c = image_tools.h5_iterative_creator(fn,
                                        overwrite_if_file_exists=True,
                                        max_img_height=1,
                                        max_img_width=2105,
                                        close_and_open_on_each_iteration=True,
                                        color_channel=False,
                                        add_to_existing_H5=False,
                                        ignore_image_range_warning=False,
                                        dtype_img = h5py.h5t.IEEE_F32LE,
                                        dtype_labels = h5py.h5t.IEEE_F32LE,
                                        image_key_name = 'final_features_2105')

    for k in tqdm(h5_file_list_to_combine):
        with h5py.File(k, 'r') as h:
            # print(h.keys())
            final_features_2105 = h['final_features_2105'][:]
            h5c.add_to_h5(final_features_2105, np.ones(final_features_2105.shape[0])*-1)
    with h5py.File(fn, 'r+') as h:
        del h['labels']

    keys = ['file_name_nums', 'frame_nums', 'full_file_names', 'in_range', 'labels',
            'locations_x_y', 'max_val_stack']

    trial_nums_and_frame_nums = []
    for k in h5_file_list_to_combine:
        print(k)
        trial_nums_and_frame_nums.append(image_tools.get_h5_key_and_concatenate(str(k), 'trial_nums_and_frame_nums'))
    trial_nums_and_frame_nums = np.hstack(trial_nums_and_frame_nums)

    with h5py.File(fn, 'r+') as h:
        for k in keys:
            print(k)
            out = image_tools.get_h5_key_and_concatenate(h5_file_list_to_combine, k)
            h[k] = out

    utils.overwrite_h5_key(fn, 'template_img', image_tools.get_h5_key_and_concatenate(h5_file_list_to_combine[0], 'template_img'))
    utils.overwrite_h5_key(fn, 'multiplier', image_tools.get_h5_key_and_concatenate(h5_file_list_to_combine[0], 'multiplier'))
    utils.overwrite_h5_key(fn, 'trial_nums_and_frame_nums', image_tools.get_h5_key_and_concatenate(h5_file_list_to_combine[0], 'trial_nums_and_frame_nums'))
    if delete_extra_files:
        for k in h5_file_list_to_combine:
            os.remove(k)


h5_bd_session = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/'
# h5_bd_session = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/untitled folder/'
h5_file_list_to_combine = [str(k) for k in utils.sort(utils.lister_it(utils.get_h5s(h5_bd_session), 'final_to_combine'))]
combine_final_h5s(h5_file_list_to_combine, delete_extra_files=False)



tmp1 = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/AH1179X23052021x1_final_combined.h5'
with h5py.File(tmp1, 'r') as h:
    for k in h.keys():
        print(k)
        try:
            print(h[k][:].shape)
        except:
            pass
        print('___')
print('___')
print('___')
print('___')
tmp1 = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/AH1179X23052021x1_final_to_combine_6_to_10_of_299.h5'
with h5py.File(tmp1, 'r') as h:
    for k in h.keys():
        print(k)
        try:
            print(h[k][:].shape)
        except:
            pass
        print('___')


h5_bd_session = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/'
utils.auto_combine_final_h5s(h5_bd_session, False)


utils.print_h5_keys('/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/untitled folder/AH1179X23052021x1_final_combined.h5')
utils.print_h5_keys('/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/untitled folder/AH1179X23052021x1_final_to_combine_1_to_5_of_299.h5')





k = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/untitled folder/AH1179X23052021x1_final_to_combine_1_to_5_of_299.h5'
k = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/untitled folder/AH1179X23052021x1_final_to_combine_1_to_5_of_299.h5'
utils.print_h5_keys(k)
trial_nums_and_frame_nums = []
trial_nums_and_frame_nums.append(image_tools.get_h5_key_and_concatenate(k, 'trial_nums_and_frame_nums'))



trial_nums_and_frame_nums = []
for k in h5_file_list_to_combine:
    print(k)
    trial_nums_and_frame_nums.append(image_tools.get_h5_key_and_concatenate(k, 'trial_nums_and_frame_nums'))


utils.auto_combine_final_h5s(h5_bd_session, False)



h5 = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/Session1_FINISHED/Session1/AH1179X23052021x1_final_combined.h5'
utils.print_h5_keys(h5)
# match the files with the contacts
utils.info(T_V_Test_dict[0])



file_name_nums_from_features = np.asarray([int(os.path.basename(k.decode("ascii", "ignore")).split('-')[-1][:-4]) for k in image_tools.get_h5_key_and_concatenate(h5, 'full_file_names')])


save_name = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1jFuXGPmP8QNNZxuCzCA8qVItvPJvg8hU/contactsMatter/final_T_V_Test_dict.pkl'
T_V_Test_dict = utils.load_obj(save_name)

import pdb
def foo_save_data(save_bd, features, labels):
    features = np.vstack(features)
    labels = np.concatenate(labels)
    np.save(save_bd+'features', features)
    np.save(save_bd+'labels', labels)

border_key = '3_border_inds'
# get same session, match all the contacts
dataset = T_V_Test_dict[0]
file_list = dataset['file_list'][:]
bd = '/Volumes/GoogleDrive-114825029448473821206/.shortcut-targets-by-id/1pUteMEgx37rAyqujJWxVN9-ywFAqaxhF/WhACC_PROCESSING_FOLDER/'
cnt=0
save_every_x = 5
for i in range(len(file_list)):
    f = dataset['file_list'][i]
    f = utils.norm_path(f)
    fn_cont = dataset['frame_nums'][i]
    contacts = dataset['contacts'][i]
    border_inds = dataset[border_key][i]
    sess = os.path.basename(os.path.dirname(f))

    # h5 from matching session
    h5 = bd+sess+'_FINISHED/'+sess
    h5 = utils.get_files(h5, '*final_combined.h5')
    assert len(h5) == 1, 'asdfasdf'
    h5 = h5[0]

    frame_nums_from_features = image_tools.get_h5_key_and_concatenate(h5, 'frame_nums')
    # below matches the contact SESSION already
    file_name_nums_from_features = np.asarray([int(os.path.basename(k.decode("ascii", "ignore")).split('-')[-1][:-4]) for k in image_tools.get_h5_key_and_concatenate(h5, 'full_file_names')])
    file_name_num_from_contacts = int(os.path.basename(f.split('-')[-1][:-4]))
    ind = np.where(file_name_num_from_contacts == file_name_nums_from_features)[0] # ind to the feature data

    if len(ind) == 0:
        print('no match\n')
        # pass # no match
    elif len(ind) > 1:
        assert False, 'more than one match this is impossible'
    else:

        if cnt//save_every_x == cnt/save_every_x:
            pdb.set_trace()
            final_features_2105_TEMP  = []
            contact_TEMP = []
            cnt=0

        cnt+=1
        ind = ind[0]
        loop_segs = np.asarray(utils.loop_segments(frame_nums_from_features, True))
        with h5py.File(h5, 'r') as h:
            final_features_2105 = h['final_features_2105'][loop_segs[0, ind]:loop_segs[1, ind]]
        # final_features_2105 = image_tools.get_h5_key_and_concatenate(h5, 'final_features_2105')
        fn_f = frame_nums_from_features[ind]
        assert fn_f == fn_cont, 'frame number miss match WTF'
        contact_TEMP.append(contacts[border_inds])
        final_features_2105_TEMP.append(final_features_2105[border_inds, :])

if cnt != save_every_x
    #save it





np.asarray(tmp1)
loop_segs = np.asarray(utils.loop_segments(frame_nums_from_features, True))



"""
chekc if file synced for samsons data

24 core convert all of the h5s into a single H5 file. 
"""
