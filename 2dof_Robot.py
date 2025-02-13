import numpy as np
from roboticstoolbox import ET, Link, Robot
from spatialmath import quaternion
from math import pi

if __name__ == '__main__':
    d1 : float = 1.0
    d2 : float = 1.0
    
    q0 : float = 0.0
    q1 : float = 0.0
    q : np.ndarray = np.array([q0, q1])
    
    A01 : ET = ET.Rz()
    A12 : ET = ET.tx(d1) * ET.Rz()
    A2f : ET = ET.tx(d2)
    
    link0: Link = Link(A01,
                      name='link0',
                      qlim=[-pi,pi],
                      parent=None,
                      jindex=0,
                      joint='R')
    
    link1: Link = Link(A12,
                      name='link1',
                      qlim=[-pi,pi],
                      parent=link0,
                      jindex=1,
                      joint='R')
    
    ef : Link = Link(A2f,
                     name='ef',
                     parent=link1)
    
    links: Link = [link0, link1, ef]
    
    robot: Robot = Robot(links, name='2dof')
    print(Robot)
    
    q[1] = pi/2
    A = robot.fkine(q)
    print(A)
    
    phi, theta, psi = A.eul()
    print(f'phi = {phi}, theta = {theta}, psi = {psi}')
    
    quat: quaternion.UnitQuaternion = A.UnitQuaternion()
    print(f'quat = {quat}')
    
    sol: tuple = robot.ik_NR(A)
    print(f'q = {np.round(sol[0], 4)}')
    
    robot.plot(q, block=True, backend='pyplot')