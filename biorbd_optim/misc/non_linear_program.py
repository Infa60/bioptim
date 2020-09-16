class NonLinearProgram:
    def __init__(
        self,
        CX=None,
        J=[],
        U=None,
        U_bounds=None,
        U_init=None,
        X=None,
        X_bounds=None,
        X_init=None,
        casadi_func={},
        control_type=None,
        dt=None,
        dynamics=[],
        dynamics_func=None,
        dynamics_type=None,
        external_forces=None,
        g=[],
        g_bounds=[],
        mapping={},
        model=None,
        nb_integration_steps=None,
        nb_threads=None,
        ns=None,
        nu=None,
        nx=None,
        ode_solver=None,
        p=None,
        par_dynamics={},
        phase_idx=None,
        plot={},
        shape={},
        t0=None,
        tf=None,
        u=None,
        var_controls={},
        var_states={},
        x=None,
    ):
        self.CX = CX
        self.J = J
        self.U = U
        self.U_bounds = U_bounds
        self.U_init = U_init
        self.X = X
        self.X_bounds = X_bounds
        self.X_init = X_init
        self.casadi_func = casadi_func
        self.control_type = control_type
        self.dt = dt
        self.dynamics = dynamics
        self.dynamics_func = dynamics_func
        self.dynamics_type = dynamics_type
        self.external_forces = external_forces
        self.g = g
        self.g_bounds = g_bounds
        self.mapping = (mapping,)
        self.model = model
        self.nb_integration_steps = nb_integration_steps
        self.nb_threads = nb_threads
        self.ns = ns
        self.nu = nu
        self.nx = nx
        self.ode_solver = ode_solver
        self.p = p
        self.par_dynamics = par_dynamics
        self.phase_idx = phase_idx
        self.plot = plot
        self.shape = (shape,)
        self.t0 = t0
        self.tf = tf
        self.u = u
        self.var_controls = var_controls
        self.var_states = var_states
        self.x = x
