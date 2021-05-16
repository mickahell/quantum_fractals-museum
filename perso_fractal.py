import streamlit as st
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from numpy import pi
import matplotlib.pyplot as plt


def app():
    st.title("Create your uniq qfractal")
    st.write("Here the creation of the fractal base")

    expander = st.beta_expander("What's happening ?")
    expander.write("Here you could put in some really, really long explanations...")

    # App code
    # Slider option
    max_shots_slider = st.sidebar.slider("Number of shots", 1, 10, 2, 1)
    if st.sidebar.checkbox('Customize the angles'):
        iterations = st.sidebar.slider("X", 0.0, 2 * pi, 0.0, 0.01)
        separation = st.sidebar.slider("Z", 0.0, 2 * pi, pi, 0.01)

    # Init Qasm simulator backend
    statevector_sim = Aer.get_backend("statevector_simulator")

    def complex_cal(qc, statevector_sim):
        statevector_job = execute(qc, statevector_sim)
        statevector_result = statevector_job.result()
        psi = statevector_result.get_statevector()
        z0 = psi[0]
        z1 = psi[1]
        if z1.real != 0 or z1.imag != 0:
            z = z0 / z1
            z = round(z.real, 2) + round(z.imag, 2) * 1j
        else:
            z = 0
        return z

    init_q = QuantumRegister(1, 'q')
    qc = QuantumCircuit(init_q)

    tab = [[], []]
    x = []
    y = []
    tab_temp = []

    shots = 100
    max_shots = max_shots_slider

    progress_bar = st.sidebar.progress(0)
    progress_bar_general = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    status_text_general = st.sidebar.empty()
    # Launch
    qc.h(init_q)
    for w in range(max_shots):
        for i in range(shots):
            qc.rx(-pi / (shots - i), init_q)
            qc.rz(pi / (shots / 8), init_q)
            z = complex_cal(qc, statevector_sim)
            if z != 0:
                tab_temp.append(z)

            progress_bar.progress(int((i + 1) * 100 / shots))
            status_text.text("%i%% Complete" % ((i + 1) * shots / 100))
        qc.barrier()

        progress_bar_general.progress(int((w + 1) * 100 / max_shots))
        status_text_general.text(f'Full circuit complete {(w + 1) * 100 / max_shots} %')
    # Done

    for i in tab_temp:
        iteration = tab_temp.count(i)
        if tab[0].count(i) < 1:
            tab[0].append(i)
            tab[1].append(iteration)

    for i in range(len(tab[0])):
        x.append(tab[0][i].real)
        y.append(tab[0][i].imag)

    st.write("Total of State Vector :", len(tab_temp))

    fig = plt.figure()
    plt.scatter(x, y, c=tab[1], s=1, cmap="coolwarm")

    st.pyplot(fig)
    progress_bar.empty()
    progress_bar_general.empty()
    status_text.empty()
    status_text_general.empty()
