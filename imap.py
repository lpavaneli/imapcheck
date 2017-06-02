#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lpavaneli - 2011

import  poplib, sys, traceback, argparse, imaplib

class IMAPCheck:

        def __init__(self, username, password, hostname, port, ssl):
                self.username = username
                self.password = password
                self.hostname = hostname
                self.port = port
                self.ssl = ssl

        def check(self):
                try:
                        if self.ssl != None:
                                M = imaplib.IMAP4(self.hostname,self.port)
                        else:
                                M = imaplib.IMAP4_SSL(self.hostname,self.port)
                        M.login(self.username,self.password)

                        Mails = M.select(mailbox='INBOX', readonly=False)

                        print "OK: %s %s emails" % (Mails[0], Mails[1])

                except Exception, err:
                        sys.stderr.write('ERROR: %s\n' % str(err))
                        return 1
                finally:
                        try:
                                M.quit()
                        except:
                                pass
                        return 0


if __name__ == '__main__':

        parser = argparse.ArgumentParser(description='Check IMAP4 Auth',formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument('-u', '--username', nargs=1, dest='username', required=True, help='usage: username@domain')
        parser.add_argument('-p', '--password', nargs=1, dest='password', required=True, help='user password')
        parser.add_argument('-H', '--hostname', nargs=1, dest='hostname', required=True, help='host ip')
        parser.add_argument('-P', '--port', type=int, nargs=1, dest='port', default=[143], help='port service')
        parser.add_argument('-s', '--ssl', type=int, nargs='?', dest='ssl', default=[0], help='enable ssl check')

        parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')


        args = parser.parse_args()
        connect = IMAPCheck(args.username[0],args.password[0],args.hostname[0],args.port[0],args.ssl)
        sys.exit(connect.check())
