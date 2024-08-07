# cli.py
import argparse
from core import PenTestFramework
RED = "\33[91m"
END= "\033[0m"
banner = f"""
  {RED}



 _____           _                          _      __                                             _                       
|_   _|         | |    _                   | |    / _|                                           | |                      
  | | ___   ___ | |   (_) __   ____ _ _ __ | |_  | |_ _ __ __ _ _ __ ___   _____      _____  _ __| | __                   
  | |/ _ \ / _ \| |       \ \ / / _` | '_ \| __| |  _| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /                   
  | | (_) | (_) | |    _   \ V | (_| | |_) | |_  | | | | | (_| | | | | | |  __/\ V  V | (_) | |  |   <                    
  \_/\___/ \___/|_|   (_)   \_/ \__,_| .__/ \__| |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\                   
                                     | |     ______                                                                       
                                     |_|    |______|                                                                      
  ___        _   _                               ___  _    ______ _____ _   _   ___                      _     _____ __   
 / _ \      | | | |                 _     ____  / _ \| |   | ___ |_   _| \ | | |_  |                    | |   |  _  /  |  
/ /_\ \_   _| |_| |__   ___  _ __  (_)   / __ \/ /_\ | |   | |_/ / | | |  \| |   | | ___  ___  ___ _ __ | |__ | |/' `| |  
|  _  | | | | __| '_ \ / _ \| '__|      / / _` |  _  | |   | ___ \ | | | . ` |   | |/ _ \/ __|/ _ | '_ \| '_ \|  /| || |  
| | | | |_| | |_| | | | (_) | |     _  | | (_| | | | | |___| |_/ /_| |_| |\  /\__/ | (_) \__ |  __| |_) | | | \ |_/ _| |_ 
\_| |_/\__,_|\__|_| |_|\___/|_|    (_)  \ \__,_\_| |_\_____\____/ \___/\_| \_\____/ \___/|___/\___| .__/|_| |_|\___/\___/ 
                                         \____/                                                   | |                     
                                                                                                  |_|                     

                                                                                                                                  
{END}"""  
print(banner)
def main():
    parser = argparse.ArgumentParser(description="Advanced Automated Penetration Testing Framework")
    parser.add_argument('module', help="Module to run")
    parser.add_argument('--target', help="Target for the module", default=None)
    parser.add_argument('--wordlist', help="Path to the wordlist (for password_cracker)", default=None)
    parser.add_argument('--config', help="Path to configuration file", default="config/settings.yaml")
    parser.add_argument('--threads', help="Number of threads for parallel processing", type=int, default=1)
    args = parser.parse_args()

    framework = PenTestFramework()

    if args.config:
        framework.config = framework.load_config()

    framework.load_module(args.module)

    result = None
    if args.module == 'network_scanner':
        result = framework.run_module(args.module, target=args.target or framework.config['default_target'])
    elif args.module == 'vuln_scanner':
        result = framework.run_module(args.module, url=args.target or framework.config['default_target'])
    elif args.module == 'password_cracker':
        hash = input("Enter the hash to crack: ")
        result = framework.run_module(args.module, hash, args.wordlist or framework.config['wordlist_path'])

    if result:
        print(result)  

if __name__ == "__main__":
    main()
