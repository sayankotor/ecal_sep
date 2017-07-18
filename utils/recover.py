import numpy as np

def get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups):
    #energy_ = 0.0
    answ = []
    for group in [ecal_data_groups, ps_data_groups]:
        try:
            energy_data = group.get_group((cell_y_new,cell_x_new))
            energy_ = energy_data['energy'].values[0]
        except:
            energy_ = 0.0
        answ.append(energy_)
    return answ
    


def make_vector_left(cell_x, cell_y, area_bound, n_area_bound, ecal_data_groups, ps_data_groups, multiplier, divider):
    vect_ = []
    vect_ps = []
    for y in [cell_y -2, cell_y -1, cell_y, cell_y +1, cell_y +2]:
        cell_x_new = n_area_bound.left
        cell_y_new = multiplier*(y - area_bound.bottom)/divider +n_area_bound.bottom
        vect_.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[0])
        vect_ps.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[1])
    return vect_,vect_ps
        
def make_vector_right(cell_x, cell_y, area_bound, n_area_bound, ecal_data_groups, ps_data_groups, multiplier, divider):
    vect_ = []
    vect_ps = []
    for y in [cell_y -2, cell_y -1, cell_y, cell_y +1, cell_y +2]:
        cell_x_new = n_area_bound.right
        cell_y_new = multiplier*(y - area_bound.bottom)/divider +n_area_bound.bottom
        vect_.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[0])
        vect_ps.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[1])
    return vect_,vect_ps
        
def make_vector_top(cell_x, cell_y, area_bound, n_area_bound, ecal_data_groups, ps_data_groups, multiplier, divider):
    vect_ = []
    vect_ps = []
    for x in [cell_x -2, cell_x -1, cell_x, cell_x +1, cell_x +2]:
        cell_x_new = multiplier*(x - area_bound.left)/divider + n_area_bound.left
        cell_y_new = n_area_bound.top
        vect_.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[0])
        vect_ps.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[1])
    return vect_,vect_ps

def make_vector_bottom(cell_x, cell_y, area_bound, n_area_bound, ecal_data_groups, ps_data_groups, multiplier, divider):
    vect_ = []
    vect_ps = []
    for x in [cell_x -2, cell_x -1, cell_x, cell_x +1, cell_x +2]:
        cell_x_new = multiplier*(x - area_bound.left)/divider + n_area_bound.left
        cell_y_new = n_area_bound.bottom
        vect_.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[0])
        vect_ps.append(get_energy(cell_x_new, cell_y_new, ecal_data_groups, ps_data_groups)[1])
    return vect_,vect_ps

def assigment_left(ecal_square, ps_square, vect_, vect_ps, distance_, type_='norm'): #type - out - norm, in - inv
    distanses = {"norm":2-distance_, "inv":2+distance_}
    ecal_square[distanses[type_], :] = vect_ #if x-coordinate change y-column
    ps_square[distanses[type_], :] = vect_ps
    
def assigment_right(ecal_square, ps_square, vect_, vect_ps, distance_,  type_='norm'):
    distanses = {"norm":2+distance_, "inv":2-distance_}
    ecal_square[distanses[type_], :] = vect_
    ps_square[distanses[type_], :] = vect_ps
    
def assigment_top(ecal_square, ps_square, vect_, vect_ps, distance_,  type_='norm'):
    distanses = {"norm":2+distance_, "inv":2-distance_}
    ecal_square[:, distanses[type_]] = np.array(vect_)#f y-coordinate change x-column
    ps_square[:, distanses[type_]] = np.array(vect_ps)
    
def assigment_bottom(ecal_square, ps_square, vect_, vect_ps, distance_,  type_='norm'):
    distanses = {"norm":2-distance_, "inv":2+distance_}
    ecal_square[:, distanses[type_]] = np.array(vect_)#if y-coordinate change x-column
    ps_square[:, distanses[type_]] = np.array(vect_ps)