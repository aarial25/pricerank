from django.shortcuts import render, HttpResponse
from .models import Record
import openpyxl

# Create your views here.

def index(request):
    records = Record.objects.all()
    return render(request, "home.html", context={"records" : records})
    

def home(request):
    records = Record.objects.all()
    return render(request, "home.html", context={"records" : records})


def uploadfile(request):
    if request.method == 'POST':
        excel_file = request.FILES['inputfile']
        fname = str(excel_file)
        if fname.split(".")[-1] == "xlsx":
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb.active
            Record.objects.all().delete()

            i = 1
            for row in worksheet.iter_rows():
                if i==1:
                    i = i+1
                    continue

                r = Record()
                r.region_port = row[0].value if row[0].value != None else "-"
                r.m_pro_class = row[1].value if row[1].value != None else "-"
                r.bussiness_class = row[2].value if row[2].value != None else "-"
                r.measure = row[3].value if row[3].value != None else "-"
                r.country_port = row[4].value if row[4].value != None else "-"
                r.meo = row[5].value if row[5].value != None else "-"
                r.type_fill = row[6].value if row[6].value != None else "-"
                r.vessel = row[7].value if row[7].value != None else "-"
                r.distributor = row[8].value if row[8].value != None else "-"
                r.vessel_segment = row[9].value if row[9].value != None else "-"
                r.emp_name = row[10].value if row[10].value != None else "-"
                r.cust_type = row[11].value if row[11].value != None else "-"
                r.cust_group = row[12].value if row[12].value != None else "-"
                r.cust_name_rev = row[13].value if row[13].value != None else "-"
                r.mode_delivery = row[14].value if row[14].value != None else "-"
                r.rtm_model = row[15].value if row[15].value != None else "-"
                r.ship_to_party = row[16].value if row[16].value != None else "-"
                r.sales_org_code = row[17].value if row[17].value != None else "-"
                r.cust_code = row[18].value if row[18].value != None else "-"
                r.period_year = row[19].value if row[19].value != None else "-"
                r.c4 = row[20].value if row[20].value != None else "-"
                r.volume = row[21].value if row[21].value != None else "-"
                r.volume_buckets = row[22].value if row[22].value != None else "-"
                r.material = row[23].value if row[23].value != None else "-"
                r.imo_number = row[24].value if row[24].value != None else "-"
                r.port = row[25].value if row[25].value != None else "-"
                r.sales_org = row[26].value if row[26].value != None else "-"
                r.banding = row[27].value if row[27].value != None else "-"
                r.cust_country = row[28].value if row[28].value != None else "-"
                r.cust_code_rev = row[29].value if row[29].value != None else "-"
                r.cust_segment = row[30].value if row[30].value != None else "-"
                r.material_code = row[31].value if row[31].value != None else "-"
                r.mpo_name = row[32].value if row[32].value != None else "-"
                r.pack_form = row[33].value if row[33].value != None else "-"
                r.rsm = row[34].value if row[34].value != None else "-"
                r.ship_party = row[35].value if row[35].value != None else "-"
                r.vessel_code = row[36].value if row[36].value != None else "-"
                r.vessel_sub_type = row[37].value if row[37].value != None else "-"
                r.volume_L15 = row[38].value if row[38].value != None else "-"
                r.c3_margin = row[39].value if row[39].value != None else "-"
                r.agent_comm = row[40].value if row[40].value != None else "-"
                r.c4_1 = row[41].value if row[41].value != None else "-"
                r.up_cpl = str(round(row[42].value, 2)) if row[42].value != None else "-"
                r.ucogs_cpl = str(round(row[43].value, 2)) if row[43].value != None else "-"
                r.udcost_cpl = str(round(row[44].value, 2)) if row[44].value != None else "-"
                r.ucost_cpl = str(round(row[45].value, 2)) if row[45].value != None else "-"
                r.uc3_cpl = str(round(row[46].value, 2)) if row[46].value != None else "-"
                r.uc4_cpl = str(round(row[47].value, 2)) if row[47].value != None else "-"
                r.non_meo = row[48].value if row[48].value != None else "-"
                r.plan_volume_L15 = row[49].value if row[49].value != None else "-"
                r.plan_c3_margin = row[50].value if row[50].value != None else "-"
                r.plan_agent_comm = row[51].value if row[51].value != None else "-"
                r.plan_c4_margin = row[52].value if row[52].value != None else "-"
                r.sum_of_cogs = row[53].value if row[53].value != None else "-"
                r.sum_of_d_cost = row[54].value if row[54].value != None else "-"
                r.sum_of_net_proc = row[55].value if row[55].value != None else "-"
                r.sum_of_non_meo = row[56].value if row[56].value != None else "-"
                r.sum_of_total_cost = row[57].value if row[57].value != None else "-"
                r.sum_of_vol_var = row[58].value if row[58].value != None else "-"
                r.use = "Y" if (row[21].value != None and int(row[21].value) > 0) else "N"
                r.save()

            return HttpResponse('File Saved')
    
        else:
            return HttpResponse('Invalid File. Please Upload Only Excel File (.xlsx)')

    return render(request, "home.html", context={"records" : Record.objects.all()})


