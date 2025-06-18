import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install Tw Team [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Tw Team"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Tw Team")
          os.system(system.sudo+" cp -r modules core Tw Team.py "+system.conf_dir+"/Tw Team")
          os.system(system.sudo+" cp -r core/Tw Team "+system.bin)
          os.system(system.sudo+" cp -r core/toolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Tw Team")
          os.system(system.sudo+" chmod +x "+system.bin+"/toolx")
          os.system("cd .. && "+system.sudo+" rm -rf Tw Team")
          if os.path.exists(system.bin+"/Tw Team") and os.path.exists(system.conf_dir+"/Tw Team"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Tw Team{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Tw Team{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/Tw Team"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Tw Team")
          os.system("cp -r modules core Tw Team.py "+system.conf_dir+"/Tw Team")
          os.system("cp -r core/Tw Team "+system.bin)
          os.system("cp -r core/toolx "+system.bin)
          os.system("chmod +x "+system.bin+"/Tw Team")
          os.system("chmod +x "+system.bin+"/toolx")
          os.system("cd .. && rm -rf Tw Team")
          if os.path.exists(system.bin+"/Tw Team") and os.path.exists(system.conf_dir+"/Tw Team"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Tw Team{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Tw Team{nc}@{blue}space {yellow}$ {nc}")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
