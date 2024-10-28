from netdem import *


def createDEM():
    p_rho = 1120
    p_size = 0.015
    write_interval = 0.01

    sim = Simulation()
    sim.domain_manager.SetBound(-0.6, -0.6, -0.6, 0.6, 0.6, 0.6)
    sim.domain_manager.SetCellSpacing(0.3, 0.3, 0.3)

    cnt_model = LinearSpring(2.0e6, 1.0e6, 0.7, 0.5)
    cnt_model_prt = sim.scene.InsertContactModel(cnt_model)
    sim.scene.SetNumberOfMaterials(1)
    sim.scene.SetCollisionModel(0, 0, cnt_model_prt)

    sphere = Sphere(p_size)
    sphere_ptr = sim.scene.InsertShape(sphere)

    p = Particle()
    p.SetShape(sphere_ptr)
    p.SetDensity(p_rho)
    p.SetPosition(0, 0, 0.0275)
    # sim.scene.InsertParticle(p)

    wall_box = WallBoxPlane(0.1, 0.1, 0.2, 0, 0, 0)
    wall_box.ImportToScene(sim.scene)

    grav = Gravity()
    grav.Init(sim)
    sim.modifier_manager.Insert(grav)
    sim.modifier_manager.Enable(grav.label)

    data_dumper = DataDumper()
    data_dumper.Init(sim)
    data_dumper.SetRootPath("dem/")
    data_dumper.SetSaveByTime(write_interval)
    data_dumper.dump_contact_info = True
    data_dumper.dump_wall_info = True
    data_dumper.dump_mesh = True
    data_dumper.SaveShapeInfoAsSTL()
    sim.modifier_manager.Insert(data_dumper)
    sim.modifier_manager.Enable(data_dumper.label)

    sim.dem_solver.timestep = 1.0e-5
    sim.enable_logging = False
    return sim
