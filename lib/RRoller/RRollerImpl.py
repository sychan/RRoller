# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import os
import uuid
from KBaseReport.KBaseReportClient import KBaseReport
#END_HEADER


class RRoller:
    '''
    Module Name:
    RRoller

    Module Description:
    A KBase module: RRoller
    This sample module contains one small method - rick_roll.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR

        # Any configuration parameters that are important should be parsed and
        # saved in the constructor.
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']

        #END_CONSTRUCTOR
        pass

    def rick_roll(self, ctx, input_params):
        """
        The actual function is declared using 'funcdef' to specify the name
        and input/return arguments to the function.  For all typical KBase
        Apps that run in the Narrative, your function should have the
        'authentication required' modifier.
        :param roll_id: instance of String
        :returns: instance of type "RRoll_Output" (Here is the definition of
           the output of the function.  The output can be used by other SDK
           modules which call your code, or the output visualizations in the
           Narrative.  'report_name' and 'report_ref' are special output
           fields- if defined, the Narrative can automatically render your
           Report.) -> structure: parameter "report_name" of String,
           parameter "report_url" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN rick_roll
        report_name = str(input_params["roll_id"])
        workspace_name = str(input_params["workspace_name"])
        print "Report name is {}".format(report_name)
        report_url = "https://www.youtube.com/watch?v=oHg5SJYRHA0"

        self.callbackURL = os.environ.get('SDK_CALLBACK_URL')
        if self.callbackURL is None:
            raise ValueError("SDK_CALLBACK_URL not set in environment")

        # build report
        #
        reportName = 'kb_rickroll_{}_{}'.format(report_name, str(uuid.uuid4()))

        reportObj = {'objects_created': [],
                     'message': '',
                     'direct_html': '',
                     'direct_html_index': 0,
                     'file_links': [],
                     'html_links': [],
                     'workspace_name': workspace_name,
                     'report_object_name': reportName
                     }

        # html report
        html_report_lines = []
        html_report_lines += ['<html>']
        html_report_lines += ["<script>"]
        html_report_lines += ['window.location.assign("https://www.youtube.com/watch?v=oHg5SJYRHA0&autoplay=on")']
        html_report_lines += ["</script>"]
        html_report_lines += ['<body bgcolor="white">']
        html_report_lines += ['<a href="{}">{}</a>'.format(report_url, report_url)]
        html_report_lines += ['</body>']
        html_report_lines += ['</html>']

        reportObj['direct_html'] = "\n".join(html_report_lines)
        SERVICE_VER = 'release'
        report = KBaseReport(self.callbackURL, token=ctx['token'], service_ver=SERVICE_VER)
        report_info = report.create_extended_report(reportObj)
        output = {'report_name': report_info['name'],
                  'report_ref': report_info['ref']}

        #END rick_roll

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method rick_roll return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
