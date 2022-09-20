from pickle import TRUE
from django.db import models

# Create your models here.

class Record(models.Model):

    # Region Of Port
    region_port = models.CharField(max_length=100, default="-")                                                 

    # Marine Product Classification
    m_pro_class = models.CharField(max_length=100, default="-")                                                 

    # Business Classification
    bussiness_class = models.CharField(max_length=100, default="-")                                             

    # Measure
    measure = models.CharField(max_length=100, default="-")                                                     

    # Country Of Port
    country_port = models.CharField(max_length=100, default="-")                                                

    # MEO / Non MEO
    meo = models.CharField(max_length=10, choices=[("MEO","MEO"), ("Non MEO", "Non MEO"), ("Others","Others")], default="MEO")                  

    # Type Of Fill
    type_fill = models.CharField(max_length=100, default="-")                                                   

    # Vessel
    vessel = models.CharField(max_length=100, default="-")                          

    # Distributor / End Customer
    distributor = models.CharField(max_length=50, choices=[("End Customer Non Index","End Customer Non Index"),("End Customer Index","End Customer Index"),("MD","MD"),("MD Distributor","MD Distributor")], default="MD")                                                 

    # Vessel Segment
    vessel_segment = models.CharField(max_length=100, default="-")                                              

    # Employee Name
    emp_name = models.CharField(max_length=100, default="-")                                                    

    # Customer Type
    cust_type = models.CharField(max_length=100, choices=[("International","International"), ("Local","Local")], default="Local")             

    # Customer Group
    cust_group = models.CharField(max_length=100, default="-")                                                  

    # Customer Name Rev
    cust_name_rev = models.CharField(max_length=100, default="-")                                               

    # Mode Of Delivery
    mode_delivery = models.CharField(max_length=100, default="-", choices=[("Barge Delivery","Barge Delivery"), ("Road Delivery","Road Delivery"), ("Not Assigned", "Not Assigned"), ("-", "-")])                                               

    # RTM Model
    rtm_model = models.CharField(max_length=100, default="-")                                                   

    # Ship To Party
    ship_to_party = models.CharField(max_length=100, default="-")                                               

    # Sales Org Code
    sales_org_code = models.CharField(max_length=100, default="-")                                               

    # Customer Code
    cust_code = models.CharField(max_length=100, default="-")                                               

    # Period/Year
    period_year = models.CharField(max_length=100, default="-")     

    # C4
    c4 = models.CharField(max_length=100, default="-")     

    # Volume
    volume = models.CharField(max_length=100, default="-")    

    # Volume Buckets
    volume_buckets = models.CharField(max_length=100, default="-")                      

    # Material
    material = models.CharField(max_length=100, default="-")                                                                                                                                                                                                       
    
    # IMO Number
    imo_number = models.CharField(max_length=100, default="-")       

    # Port
    port = models.CharField(max_length=100, default="-")               

    # Sales Organization
    sales_org = models.CharField(max_length=100, default="-")                     

    # Banding
    banding = models.CharField(max_length=100, default="-")                  

    # Country Of Customer
    cust_country = models.CharField(max_length=100, default="-")                                               

    # Customer Code Rev
    cust_code_rev = models.CharField(max_length=100, default="-")                                               

    # Customer Segment
    cust_segment = models.CharField(max_length=100, default="-")                

    # Material Code
    material_code = models.CharField(max_length=100, default="-")                                                                              

    # MPO Name
    mpo_name = models.CharField(max_length=100, default="-")                                               

    # Pack From
    pack_form = models.CharField(max_length=100, default="-")                                               

    # RSM
    rsm = models.CharField(max_length=100, default="-")                                               

    # Sales Org Code
    sales_org_code = models.CharField(max_length=100, default="-")                                               

    # Ship To Part Name
    ship_party = models.CharField(max_length=100, default="-")                                               

    # Vessel Code
    vessel_code = models.CharField(max_length=100, default="-")                                               

    # Vessel Sub Type
    vessel_sub_type = models.CharField(max_length=100, default="-")                         

    # Volume L15
    volume_L15 = models.CharField(max_length=100, default="-")                                               

    # C3 Margin
    c3_margin = models.CharField(max_length=100, default="-")                                               

    # Agents Commission
    agent_comm = models.CharField(max_length=100, default="-")      

    # C4 1
    c4_1 = models.CharField(max_length=100, default="-")              

    # UP(CPL)
    up_cpl = models.CharField(max_length=100, default="-")                                                                                                                         

    # UCOGS(CPL)
    ucogs_cpl = models.CharField(max_length=100, default="-")                                               

    # UDCost(CPL)
    udcost_cpl = models.CharField(max_length=100, default="-")                                               

    # UCost(CPL)
    ucost_cpl = models.CharField(max_length=100, default="-")                                               

    # UC3(CPL)
    uc3_cpl = models.CharField(max_length=100, default="-")                      

    # UC4(CPL)
    uc4_cpl = models.CharField(max_length=100, default="-")                                              

    # Non MEO
    non_meo = models.CharField(max_length=100, default="-")                                               

    # Plan Volume L15
    plan_volume_L15 = models.CharField(max_length=100, default="-")                                               

    # Plan C3 Margin
    plan_c3_margin = models.CharField(max_length=100, default="-")                                               

    # Plan Agent Comm
    plan_agent_comm = models.CharField(max_length=100, default="-")                                               

    # Plan C4 Margin
    plan_c4_margin = models.CharField(max_length=100, default="-")                                               

    # Sum Of Cogs
    sum_of_cogs = models.CharField(max_length=100, default="-")                                               

    # Sum of D Cost
    sum_of_d_cost = models.CharField(max_length=100, default="-")                                               

    # Sum Of Net Proc
    sum_of_net_proc = models.CharField(max_length=100, default="-")                                               

    # Sum Of Non Meo Volumes
    sum_of_non_meo = models.CharField(max_length=100, default="-")                                               

    # Sum of total cost
    sum_of_total_cost = models.CharField(max_length=100, default="-")                                               

    # Sum Of Volume Var
    sum_of_vol_var = models.CharField(max_length=100, default="-")                                               

    # Use
    use = models.CharField(max_length=100, default="N", choices=[("Y","Y"),("N","N")])                                               




