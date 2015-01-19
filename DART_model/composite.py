from fractions import Fraction


def composite_order(list_list):  
    # Why doesn't this work??:  
    # superlist = sum(list for list in list_list)
    superlist = []
    for list in list_list:
        superlist += list
    return sorted(superlist)
    

def get_onset_times(durational_values_list):
    onset_times = [0]
    for duration in durational_values_list[:-1]:
        onset_times.append(onset_times[-1] + duration)
    return onset_times

