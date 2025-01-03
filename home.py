import streamlit as st

def apps():
    st.title("Welcome to Waste Classifier")
    st.write("This application helps you classify different types of waste using machine learning.")
    st.write("Here's how it works:")

    st.header("1. Recycling Process")
    st.write("Recycling is the process of converting waste materials into new materials and objects. It helps in reducing the consumption of fresh raw materials, energy usage, air pollution, and water pollution.")
    st.image("recycling_process.png", caption="Recycling Process", use_column_width=True)
    st.write("Approximately 6 Million Tonnes of Plastic Waste goes un-recycled every year in India.")
    st.write("The idea of reusing products has been around for quite some time. Though the plastic recycling process has its limitations and flaws, it is a constantly evolving process. Of the 7 major types of plastics that are largely available, these four are most commonly recycled:")
    st.write("- PET (Polyethylene Terephthalate)")
    st.write("- HDPE (High Density Polyethylene)")
    st.write("- PVC (Polyvinyl Chloride)")
    st.write("- LDPE (Low Density Polyethylene)")
    st.write("Like all recycling processes, the plastic recycling process refers to the process of re-using plastic waste by means like reprocessing. Due to the low biodegradability of plastics, understanding the recycling process has become essential.")

    st.header("Plastic Recycling Process")
    st.write("The recycling processes can be broken down into 7 distinct steps:")
    
    st.subheader("Step 1 - Collection")
    st.write("Plastic waste is growing by the ton every day. Using a country-wide network for collection of plastic waste through rag pickers, waste collectors and waste dealers and recycling enterprises this plastic waste is collected and brought to the Sorting facilities for further processing.")

    st.subheader("Step 2 - Sorting")
    st.write("This second step is the most crucial one as he actual plastic recycling process starts with Sorting. Sorting of different plastics occurs based on:")
    st.write("- Color")
    st.write("- Resin Content")
    st.write("- Plastic Recycling Code")
    st.write("Sorting helps identify and eliminate contaminants. The process may employ manual methods or the use of specifically designed machines.")

    st.subheader("Step 3 - Shredding")
    st.write("Once the recyclable plastics have been sorted, they go through the shredder. The shredder grinds and cuts the plastics into tiny pieces. After going through shredding, heavier and lighter plastics are separated using specially designed machines. This separation helps segregate different plastics.")

    st.subheader("Step 4 - Cleaning")
    st.write("The process of Sorting and Shredding ensures that the correct types of plastics are being processed and assorted together for further processing. After a complete separation, the flakes or chunks are then washed thoroughly with detergents to remove the remaining contamination.")
    st.write("Following the cleaning process, the plastic flakes are subjected to moderate heat so that they can dry.")

    st.subheader("Step 5 - Melting")
    st.write("Post drying, the plastic flakes are melted down under regulated temperatures. The regulation of temperatures ensures that the plastics are melted without getting destroyed. On melting, these plastics are extruded and resized to be processed into granules which will later be compressed into pellets.")

    st.subheader("Step 6 - Pellet Making")
    st.write("To enable the plastics to be reusable processed granules are compressed into tiny pellets. These pellets are also known as nurdles. Pellets also enable storing similar types of plastics based on color, types of resin along with easy distribution.")

    st.subheader("Step 7 - Re-Using")
    st.write("It is important to note that, pellets recycled from particular types of plastics cannot to be re-used to make the same kinds of plastics. Instead, they are re-purposed and redesigned into other useful products.")


if __name__ == "__main__":
    apps()
