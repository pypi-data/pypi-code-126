#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports 
from scipy.signal import butter
import numpy as np
from scipy import signal as sg
from scipy.signal import find_peaks
from scipy.signal import butter, sosfiltfilt
import scipy.signal


# In[2]:


#signal filteration
                    
def filter_signal(dataset,lowcut, highcut, fs, order=5):
    y=butter_bandpass_filter(dataset, lowcut, highcut, fs, order)
    y=movingaverage(y)
    return y
    
def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfiltfilt(sos, data)
        return y
    
def movingaverage(data, periods=4):
    result = []
    data_set = np.asarray(data)
    weights = np.ones(periods) / periods
    result = np.convolve(data_set, weights, mode='valid')
    return result


# In[3]:


# Peak detection

## first method The local maxima method (LMM)

def lmm_peakdetection(data,fs):
    
    peak_final = []
    peaks, _ = find_peaks(data,height=0)
    
    for peak in peaks:
        if data[peak] > 0:
            peak_final.append(peak)
        
    return peak_final

## second method The block generation with the mean of the signal threshold method (BGM)

def threshold_peakdetection(dataset, fs):
    
    window = []
    peaklist = []
    point_index = 0
    PPI_threshold = np.ceil(0.36 * fs)
    npeaks = 0
    peakarray = []
    
    signal_mean = np.average(dataset)
    
    for point in dataset:

        if (point < signal_mean) and (len(window) < 1):
            point_index += 1
        elif (point >= signal_mean):
            window.append(point)
            point_index += 1
        else:
            maximum = max(window)
            beatposition = point_index - len(window) + (window.index(max(window)))
            peaklist.append(beatposition)
            window = []
            point_index += 1

            
    ### Ignore if the previous peak was within 360 ms interval becasuse it is T-wave
    
    for current_peak in peaklist:
        if npeaks > 0:
            prev_peak = peaklist[npeaks - 1]
            PPI = current_peak - prev_peak
            if PPI > PPI_threshold:
                peakarray.append(PPI)
        else:
            peakarray.append(current_peak)
            
        npeaks += 1    


    return peaklist

## Thied method first derivative with an adaptive threshold method (FDA) 

### divides the signal into every 5s and generates blocks

def data_segmentation (data , fs):
    segmants=[]
    for start in range (0,len(data)-1,5*fs):
        segmants.append(data[start:start + 5*fs])
    
    return segmants
    
def first_derivative_with_adaptive_ths(data, fs):
    
        peaks=[]
        th_wndw_size = 2 *fs
        block_size= 5 * fs
        blocks = data_segmentation(data,fs)
        prev_indx = -300
        for Block_indx,block in enumerate(blocks):
            
            ### The threshold is adaptively set according to the mean of amplitude in the 2s of the block
            threshold = np.mean(block[0:th_wndw_size])
            firstDeriv = block[1:] - block[:-1]
            
            for i in range(1,len(firstDeriv)):
                
                ### if the point has a differential value of zero it's extracted as peak candidates.
                
                if firstDeriv[i] <= 0 and firstDeriv[i-1] > 0:
                
                ### The peak candidates with larger amplitudes than the threshold become the peak point
                
                    if block[i] > threshold:
                        indx = block_size* Block_indx + i
                    
                    ### Ignore if the previous peak was within 360 ms interval becasuse it is T-wave
                        if indx - prev_indx > (300*fs/1000):
                            peaks.append(indx)
                            prev_indx = indx
                                                
        return peaks

## fourth method The slope sum function with an adaptive threshold method (SFA) 
def determine_peak_or_not(prevAmp, curAmp, nextAmp):
    if prevAmp < curAmp and curAmp >= nextAmp:
        return True
    else:
        return False
    
def onoff_set(peak, sig):     # move peak from dy signal to original signal   
    onoffset = []
    for p in peak:
        for i in range(p, 0,-1):
            if sig[i] == 0:
                onset = i
                break
        for j in range(p, len(sig)):
            if sig[j] == 0:
                offset = j
                break
        if onset < offset:
            onoffset.append([onset,offset])
    return onoffset
    

def slope_sum_function(data,fs):
    
    dy = [0]
    
    dy.extend(np.diff(data))
    
    w = fs // 16
    dy_ = [0] * w
    for i in range(len(data)-w):
        sum_ = np.sum(dy[i:i+w])
        if sum_ > 0:
            dy_.append(sum_)
        else:
            dy_.append(0)
    
    #init_ths = 0.7 * np.max(dy[:3*fs])
    init_ths = np.mean(dy)
    ths = init_ths
    recent_5_peakAmp = []
    peak_ind = []
    bef_idx = -300
    
    for idx in range(1,len(dy_)-1):
        prevAmp = dy_[idx-1]
        curAmp = dy_[idx]
        nextAmp = dy_[idx+1]
        if determine_peak_or_not(prevAmp, curAmp, nextAmp) == True:
            if (idx - bef_idx) > (300 * fs /1000):  # Ignore if the previous peak was within 300 ms interval
                if len(recent_5_peakAmp) < 5:  
                    if curAmp > ths:
                        peak_ind.append(idx)
                        bef_idx = idx
                        recent_5_peakAmp.append(curAmp)
                elif len(recent_5_peakAmp) == 5:
                    ths = 0.7*np.median(recent_5_peakAmp)
                    if curAmp > ths:
                        peak_ind.append(idx)
                        bef_idx = idx
                        recent_5_peakAmp.pop(0)
                        recent_5_peakAmp.append(curAmp)
                        
    onoffset = onoff_set(peak_ind, dy_)
    corrected_peak_ind = []
    for onoff in onoffset:
        segment = data[onoff[0]:onoff[1]]
        corrected_peak_ind.append(np.argmax(segment) + onoff[0])
                    
    return corrected_peak_ind

#fifth method Event-Related Moving Averages with Dynamic Threshold

## moving_average function used from NeuroKit2: The Python Toolbox for Neurophysiological Signal Processing  
##link https://neurokit2.readthedocs.io/en/latest/_modules/neurokit2/signal/signal_smooth.html
def moving_average(signal, kernel='boxcar', size=5):

    # Get window.
    window =sg.get_window(kernel, size)
    w = window / window.sum()

    # Extend signal edges to avoid boundary effects.
    x = np.concatenate((signal[0] * np.ones(size), signal, signal[-1] * np.ones(size)))

    # Compute moving average.
    smoothed = np.convolve(w, x, mode="same")
    smoothed = smoothed[size:-size]
    return smoothed


def moving_averages_with_dynamic_ths(signals,sampling_rate=50 ,peakwindow=.111, 
                                     beatwindow=.667, beatoffset=.02, mindelay=.3):
    
    signal = signals.copy()
    # ignore the samples with n
    signal[signal < 0] = 0
    sqrd = signal**2
    
    # Compute the thresholds for peak detection. Call with show=True in order
    # to visualize thresholds.
    ma_peak_kernel = int(np.rint(peakwindow * sampling_rate))
    ma_peak = moving_average(sqrd, size=ma_peak_kernel)
    
    ma_beat_kernel = int(np.rint(beatwindow * sampling_rate))
    ma_beat = moving_average(sqrd, size=ma_beat_kernel)

    
    thr1 = ma_beat + beatoffset * np.mean(sqrd)    # threshold 1

    # Identify start and end of PPG waves.
    waves = ma_peak > thr1
   
    beg_waves = np.where(np.logical_and(np.logical_not(waves[0:-1]),
                                        waves[1:]))[0]
    end_waves = np.where(np.logical_and(waves[0:-1],
                                        np.logical_not(waves[1:])))[0]
    # Throw out wave-ends that precede first wave-start.
    end_waves = end_waves[end_waves > beg_waves[0]]

    # Identify systolic peaks within waves (ignore waves that are too short).
    num_waves = min(beg_waves.size, end_waves.size)
    min_len = int(np.rint(peakwindow * sampling_rate))    # threshold 2
    min_delay = int(np.rint(mindelay * sampling_rate))
    peaks = [0]

    for i in range(num_waves):

        beg = beg_waves[i]
        end = end_waves[i]
        len_wave = end - beg

        if len_wave < min_len: # threshold 2
            continue


        # Find local maxima and their prominence within wave span.
        data = signal[beg:end]
        locmax, props = scipy.signal.find_peaks(data, prominence=(None, None))

        if locmax.size > 0:
            # Identify most prominent local maximum.
            peak = beg + locmax[np.argmax(props["prominences"])]
            # Enforce minimum delay between peaks(300ms)
            if peak - peaks[-1] > min_delay:
                peaks.append(peak)

    peaks.pop(0)

    peaks = np.asarray(peaks).astype(int)
    return peaks


# sixth method :- The mountaineer's method for peak detection in photoplethysmographic signals
def mountaineers_method(ppg):
    threshold =6
    possible_peak = False
    possible_valley =False
    upsteps=0
    value_possible_valley=0
    possible_min=False
    peaks=[]
    valleys=[]
    for i in range(0,len(ppg)):
        if i >=1:
            if ppg[i] > ppg[i-1]:
                upsteps+=1
                if possible_valley == False:
                    possible_valley=True
                    indx_possible_valley=i-1
            else:
                if upsteps >= threshold :
                     possible_peak = True
                     indx_possible_peak =i-1
                else :
                    if possible_valley == True :
                        if ppg[i] <=ppg[indx_possible_valley]:
                            indx_possible_valley=i
                if possible_peak ==True :
                    if ppg[i-1] > ppg[indx_possible_peak] : 
                        if len(peaks) ==0 or abs(i-1-peaks[-1]) >= 15:
                            peaks.append(i-1)
                        else:
                            if ppg[peaks[-1]] < ppg[i-1]:
                                  peaks[-1]=i-1                           
                    else:
                        if len(peaks) ==0 or abs(indx_possible_peak-peaks[-1]) >= 15:
                            peaks.append(indx_possible_peak)
                        else :
                            if ppg[peaks[-1]] < ppg[indx_possible_peak]:
                                peaks[-1]=indx_possible_peak
                    if possible_valley == True :
                        if len(valleys) ==0 or abs(i-1-valleys[-1]) >= 18:
                            valleys.append(indx_possible_valley)
                        else:
                            if ppg[valleys[-1]] > ppg[indx_possible_valley]:
                                  peaks[-1]=indx_possible_valley
                        possible_valley=False

                    threshold=0.6*upsteps
                    possible_peak = False
                
                upsteps=0
        
    return peaks
def ensemble_peak(preprocessed_data, fs, ensemble_ths=4):
    
    peak1 = threshold_peakdetection(preprocessed_data,fs)
    peak2 = slope_sum_function(preprocessed_data, fs)
    peak3 = first_derivative_with_adaptive_ths(preprocessed_data, fs)
    peak4 = moving_averages_with_dynamic_ths(preprocessed_data,fs)
    peak5 = lmm_peakdetection(preprocessed_data,fs)
    peak6 = mountaineers_method(preprocessed_data)
    
    peak_dic = dict()
    
    # these few lines just a voting mechanism for peaks
    #the more the peak appear in different methods the more 
    #it takes votes the more propability for it be a true peak
    
    for key in peak1:
        peak_dic[key] = 1

    for key in peak2:
        if key in peak_dic.keys():
            peak_dic[key] += 1
        else:
            peak_dic[key] = 1
    
    for key in peak3:
        if key in peak_dic.keys():
            peak_dic[key] += 1
        else:
            peak_dic[key] = 1
        
    for key in peak4:
        if key in peak_dic.keys():
            peak_dic[key] += 1
        else:
            peak_dic[key] = 1
        
    for key in peak5:
        if key in peak_dic.keys():
            peak_dic[key] += 1
        else:
            peak_dic[key] = 1
    
    for key in peak6:
        if key in peak_dic.keys():
            peak_dic[key] += 1
        else:
            peak_dic[key] = 1
        
    peak_dic = dict(sorted(peak_dic.items()))

    current_peak = 0
    prev_key = 0
    margin = 1 # min distance between two sucessive peaks

    new_peak_dic = dict()

    for key in peak_dic.keys():
        if current_peak == 0:
            new_peak_dic[key] = peak_dic[key]
        else:
            # if two peaks are too close to each others we merge them and make single peak out of them
            # which has the postion of the peak with biggest number of votes   
            if prev_key + margin >= key:
                # if prev peak has more votes we ignore current peak and add its vote to the prev one
                # and vice versa
                if peak_dic[prev_key] > peak_dic[key]: 
                    new_peak_dic[prev_key] += peak_dic[key]
                else:
                    new_peak_dic[key] = peak_dic[key] + peak_dic[prev_key] 
                    del(new_peak_dic[prev_key])
                    prev_key = key
            else:
                # if not too close just add the new peak with its votes
                new_peak_dic[key] = peak_dic[key]
                prev_key = key
        current_peak += 1
    
    ensemble_dic = dict()
    # we decide which peaks to take or ignore after last filteration process
    # by chossing min number of votes should the peak has to be accepted as a true peak
    # otherwise it considered as a false one and ignored 
    #threhold usually taken less than total number of peak detection methods by 1 or 2
    #not more than and it can't be taken equall to number of peak detection methods
    for (key, value) in new_peak_dic.items():
        if value >= ensemble_ths:
            ensemble_dic[key] = value
            
    final_peak = list(ensemble_dic.keys())
    
    return final_peak
            


# In[4]:


# heart rate calculation

def PPI_calculation(peaks,fs):
    PPI_list=[]
    PPI_list_final=[]
    for i in range(0,len(peaks)-2):
        PPI=(peaks[i+1]-peaks[i])      # difference between peaks in samples
        PPI_ms= (PPI /fs)*1000         # difference between peaks in ms
        PPI_list.append(PPI_ms)
        
    PPI_mean=np.mean(PPI_list)
    
    for PPI in PPI_list:
        # ppi value should be near to the mean value maybe not more than 300 ms 
        
        if PPI > PPI_mean-300 and PPI < PPI_mean + 300 :
            PPI_list_final.append(PPI)
            
    return PPI_list_final
            

def heartrate_calculation(peaks,fs):
    PPI_list=PPI_calculation(peaks,fs)
    HR=[]
    window_size=3
    for val in PPI_list:
        if val > 400 and val < 1200 :
            heart_rate=60000/val        #60000 ms =1 minute , val is ppi in ms
            
        elif (val > 0 and val < 400) or val > 1200:
                if len(HR) > 0:
                     # use the mean of last 10 heart-rate values calculated from the data so far:
                    heart_rate = np.mean(HR[-window_size:])
                else:
                    #heart_rate = 60.0
                    pass
        else:
            # Get around division by 0 error
            print("err")
            #heart_rate = 0.0

        HR.append(heart_rate)
        mean_hr=np.mean(HR)
        
    return mean_hr,HR
        
