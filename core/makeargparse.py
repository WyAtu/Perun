#!/usr/bin/env python
# -*- coding:utf-8 -*-

def make_argparse():
    parser = ArgumentParser(description="%(prog)s")
    parser.add_argument('-t', '--target', type=str, nargs='+', help="set the Target/CIDR/IPA-IPB/File")
    parser.add_argument('-p', '--port', type=str, nargs='+', default=DEFAULT_PORTS_LIST, help="set the Port/PortA-PortB")
    parser.add_argument('--timeout', type=int, default=3, help="set the Timeout")
    parser.add_argument('--thread', type=int, default=200, help="set the Thread")
    parser.add_argument('-l','--load-file-path', type=str, help="set the Load_File_Path")
    parser.add_argument('--vuln', type=str, nargs='+', default=[], help="select the Vuln/Vulns to check")
    parser.add_argument('--all-list', action="store_true", help="list all support Vulns" )
    parser.add_argument('--selected-vuln', action="store_true", help="show the selected Vuln/Vulns and info")
    parser.add_argument('--search', type=str, nargs='+', default="", help="set keyword/keywords to search the Vuln/Vulns that meet the condition(or)")
    parser.add_argument('--filter', type=str, nargs='+', default="", help="set keyword/keywords to search the Vuln/Vulns that meet the condition(and)")
    parser.add_argument('--exclude', type=str, nargs='+', default="", help="exclude the specified Vuln/Vulns")
    parser.add_argument('--set-port', type=str, nargs='+', default="", help="set the Port/PortA-PortB to the Vuln/Vulns that meet the condition")
    parser.add_argument('--search-list', action="store_true", help="list the info of matching Vuln/Vulns by search" )
    parser.add_argument('--user-path', type=str, default="", help="set user_dict path to crack some app with weakpwd")
    parser.add_argument('--pass-path', type=str, default="", help="set pass_dict path to crack some app with weakpwd")
    parser.add_argument('--add-web-path', type=str, default="", help="add web path to url for web scan")
    parser.add_argument('--skip-ping', action="store_true", help="skip the ping scan")
    parser.add_argument('--report', type=str, default=str(str(time())+'.html'), help="set the report name")
    parser.add_argument('--skip-report', action="store_true", help="skip generate the report")
    args = parser.parse_args()
    return vars(args)

globals()['make_argparse'] = make_argparse