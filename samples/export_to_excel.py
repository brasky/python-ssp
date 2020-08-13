import argparse
try:
    from ssp import SSP
    from openpyxl import Workbook
except:
    print("Please install the requirements from export_to_excel_requirements.txt")

def main(ssp_path, out_file):
    
    ssp = SSP(ssp_path)
    
    workbook = Workbook()
    worksheet = workbook.active

    ssp_columns = ["Control Number", "Responsible Role", "Implementation Status", "Control Origination", "Implementation"]

    worksheet.insert_cols(0, len(ssp_columns))
    worksheet.append(ssp_columns)

    for control in ssp:
        for part in control:
            try:
                row = [control.number, control.responsible_role, ", ".join(control.implementation_status), ", ".join(control.control_origination), control.part(part).text]
                worksheet.append(row)
            except Exception as e:
                print(str(e))

    workbook.save(out_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ssp', help='Path to SSP', required=True)
    parser.add_argument('--out', help='Path to SSP', required=True)
    args = parser.parse_args()

    main(args.ssp, args.out)