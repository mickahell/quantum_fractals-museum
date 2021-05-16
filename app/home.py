import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def call_csv(name_csv, zoom_in, cmap="coolwarm"):
    # CSV reading
    csv_testing = pd.read_csv(name_csv, header=None)
    x_csv = []
    y_csv = []
    ite_csv = []

    for i in range(len(csv_testing[0])):
        x_csv.append(csv_testing[0][i])
        y_csv.append(csv_testing[1][i])
        ite_csv.append(csv_testing[2][i])

    # Zoom
    gen_tab = [[], [], []]
    for i in range(len(x_csv)):
        if (-zoom_in < x_csv[i] < zoom_in) and (-zoom_in < y_csv[i] < zoom_in):
            gen_tab[0].append(x_csv[i])
            gen_tab[1].append(y_csv[i])
            gen_tab[2].append(ite_csv[i])

    mpl.rcParams.update(mpl.rcParamsDefault)
    fig = plt.figure()
    plt.axis('off')
    fig.patch.set_alpha(0)
    plt.scatter(gen_tab[0], gen_tab[1], c=gen_tab[2], s=1, cmap=cmap)

    return fig


def app():
    st.title('Welcome in the Quantum Fractals Museum')

    # State Vector qfractals
    st.write("## State Vector")

    ####################################################################################################################
    # Gal 01
    st.write("### Uniq cercle")
    left_column, right_column = st.beta_columns(2)

    # Mobius Strip
    column = left_column
    column.write("#### Möbius Strip")
    mobius = call_csv("data/statevector/unlimit_band_10.csv", 100)
    left_column.pyplot(mobius)
    expander_mobius = column.beta_expander("What's about ?")
    expander_mobius.write("100k points : Here put description, math equation and circuit")

    # Eclipse
    column = right_column
    column.write("#### Eclipse")
    eclipse = call_csv("data/statevector/1qubit_base0_1part_100.csv", 2)
    column.pyplot(eclipse)
    expander_eclipse = column.beta_expander("What's about ?")
    expander_eclipse.write("100k points : Here put description, math equation and circuit")

    # Comete
    column = left_column
    column.write("#### Comete")
    comete = call_csv("data/statevector/1qubit_baseH_1part_100.csv", 2)
    column.pyplot(comete)
    expander_comete = column.beta_expander("What's about ?")
    expander_comete.write("100k points : Here put description, math equation and circuit")

    # The Eye
    column = right_column
    column.write("#### The Eye")
    eye = call_csv("data/statevector/1qubit_baseH_halfZ_1part_100.csv", 100)
    column.pyplot(eye)
    expander_eye = column.beta_expander("What's about ?")
    expander_eye.write("100k points : Here put description, math equation and circuit")

    ####################################################################################################################
    # Gal 02
    st.write("### Rediscover the nature")
    left_column, right_column = st.beta_columns(2)

    # Foot print
    column = left_column
    column.write("#### UV Footprint")
    foot = call_csv("data/statevector/1qubit_baseH_spiral_1part_100.csv", 0.5, "plasma")
    column.pyplot(foot)
    expander_foot = column.beta_expander("What's about ?")
    expander_foot.write("100k points : Here put description, math equation and circuit")


