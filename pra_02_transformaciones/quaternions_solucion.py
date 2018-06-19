
# coding: utf-8

# ## Quaternions
# 

# In the following exercise you'll implement functions to convert between Euler angles and quaternion representations. It's useful to be able to easily navigate back and forth between these representations because of their relative strengths. Quaternions are better for calculations, while Euler angles are far more intuitive.
# 
# Some messages coming from your drone in simulation (or in the real world) will represent orientation data as a quaternion, while others use Euler angles. So it's a good idea to be able to seamlessly handle both. 
# 
# The [`udacidrone` API imlementation](https://github.com/udacity/udacidrone/blob/master/udacidrone/connection/message_types.py#L189-L284) that you're using for the projects in this program already has these conversions implemented under the hood so that's a great place to start if you aren't sure how to complete this exercise!

# In[11]:


import numpy as np
import math as mt

def quaternion_multiply(quaternion1, quaternion0):
    w0, x0, y0, z0 = quaternion0
    w1, x1, y1, z1 = quaternion1
    return np.array([-x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
                     x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
                     -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
                     x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0])

def rot_yaw_to_quat(psi):
    return np.array([mt.cos(psi/2),0,0,mt.sin(psi/2)])

def rot_pitch_to_quat(theta):
    return np.array([mt.cos(theta/2),0,mt.sin(theta/2),0])

def rot_roll_to_quat(phi):
    return np.array([mt.cos(phi/2),mt.sin(phi/2),0,0])


def euler_to_quaternion(angles):
    roll = angles[0]
    pitch = angles[1]
    yaw = angles[2]
    # TODO: complete the conversion
    # and return a numpy array of
    # 4 elements representing a quaternion [a, b, c, d]
    
    # assuming rotation by x then by y and finally by z
    q_yaw = rot_yaw_to_quat(yaw)
    q_pitch = rot_pitch_to_quat(pitch)
    q_roll = rot_roll_to_quat(roll)
    return quaternion_multiply(q_yaw, quaternion_multiply(q_pitch, q_roll))

def quaternion_to_euler(quaternion):
    a = quaternion[0]
    b = quaternion[1]
    c = quaternion[2]
    d = quaternion[3]
    
    # TODO: complete the conversion
    # and return a numpy array of
    # 3 element representing the euler angles [roll, pitch, yaw]
    return np.array([ mt.atan2(2*(a*b+c*d),1-2*(b**2 + c**2)),
                     mt.asin(2*(a*c-d*b)),
                     mt.atan2(2*(a*d+b*c),1-2*(c**2+d**2))])


# Test the conversion.

# In[16]:


euler = np.array([np.deg2rad(90), np.deg2rad(30), np.deg2rad(0)])
print(euler)

q = euler_to_quaternion(euler) # should be [ 0.683  0.683  0.183 -0.183]
print(q)

# should be [ 1.570  0.523  0.]
e = quaternion_to_euler(q)
print(e)


# Here's our [solution](/notebooks/Quaternions-Solution.ipynb)!
