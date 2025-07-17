# Developer: Engr. Tufail Mabood
# WhatsApp: +923440907874

import os
import math
import pandas as pd

def compute_concrete_properties(fck):
    """Compute concrete properties according to EC2 and MC2010 for a given fck (MPa)."""
    fcm = fck + 8
    E = 22 * (fcm / 10) ** 0.3 * 1000
    nu = 0.20

    if fck <= 50:
        fctm = 0.3 * fck ** (2 / 3)
    else:
        fctm = 2.12 * math.log(1 + fcm / 10)

    GfIt = 73 * (fcm / 10) ** 0.18
    GfIc = 100 * GfIt
    ec1 = 0.7 * fcm ** 0.31 / 1000

    if fck <= 50:
        ecu1 = 0.0022
    elif 50 < fck <= 90:
        ecu1 = (2.6 + 35 * ((90 - fck) / 100) ** 4) / 1000
    else:
        ecu1 = 0.0026

    return {
        "props(1)": E,
        "props(2)": nu,
        "props(3)": fctm,
        "props(4)": 0.0,  
        "props(5)": GfIt,
        "props(6)": GfIc,
        "props(7)": 0.0,  
        "props(8)": 0.001,  
        "props(9)": 1.0,  
        "props(10)": 1.0,  
        "props(11)": 0.0,  
        "props(12)": 0.1,  
        "props(13)": 0.1,  
        "props(14)": 0.0,  
        "props(15)": 0.0,  
        "props(16)": 0.0,  
        "props(17)": 0.0,  
        "props(18)": 0.0,  
        "props(19)": ec1,
        "props(20)": ecu1,
        "props(21)": fcm  
    }

def save_to_excel(fck):
    """Save computed properties for a given fck value in an Excel file in the current directory."""
    psi_strength = round(fck * 145.038, 2)  # Conversion from MPa to PSI
    props = compute_concrete_properties(fck)
    df = pd.DataFrame(props.items(), columns=["Property", "Value"])

    file_name = f"fck_{fck}MPa_{psi_strength}PSI.xlsx"
    file_path = os.path.join(os.getcwd(), file_name)
    df.to_excel(file_path, index=False)

    print(f"\nFile saved: {file_name} in {os.getcwd()}")

if __name__ == "__main__":
    try:
        fck_input = float(input("Enter the concrete strength (fck) in MPa: "))
        if 1 <= fck_input <= 200:
            save_to_excel(fck_input)
        else:
            print("Please enter a value between 1 and 200 MPa.")
    except ValueError:
        print("Invalid input! Please enter a numerical value.")
