class ArgumentAdder:
    """Adds arguments to parsers.

    This class serves as an abstraction of logic for adding 
    arguments to argument parsers of the argparse library.

    Attributes:
        platforms: The supported platforms for SDK generation.
            The user is allowed to input one of these values as
            the input of the --platform argument.
        arguments: A dictionary of command line arguments this
            program uses and their configurations.
    """

    platforms = [
        'cs_portable_net_lib', 
        'java_eclipse_jre_lib',
        'java_gradle_android_lib',
        'objc_cocoa_touch_ios_lib',
        'angular_javascript_lib',
        'ruby_generic_lib',
        'python_generic_lib',
        'php_generic_lib',
        'node_javascript_lib',
        'go_generic_lib'
    ]

    arguments = {
        '--api-key': {
            'required': True, 
            'help': "The API integration key from APIMatic."
        },
        '--email': {
             'required': True, 
             'help': 'Your APIMatic account email address.'
        },
        '--password': {
            'required': True, 
            'help': 'Your APIMatic account password.'
        },
        '--url': {
            'help': 'The URL of the API description.'
        },
        '--file': {
            'help': 'The path of the API description.'
        },
        '--platform': {
            'required': True, 
            'choices': platforms, 
            'help': 'The platform for which the SDK needs to be generated. Options are: ' + ', '.join(platforms), 
            'metavar': 'PLATFORM'
        },
        '--output': {
            'default': './downloads', 
            'help': 'The path of the folder in which to download files. Default is ./downloads.'
        },
        '--name': {
            'required': True,
            'help': 'The name of the SDK.'
        }
    }

    @classmethod
    def add_argument(cls, obj, argument):
        """Adds an argument.

        Takes a parser or a group object and adds the argument
        to it with the options it gets from the arguments dict.

        Args:
            obj: A parser or a group object to which the argument
                is to be added.
            argument: The argument to add.
        """
        options = ArgumentAdder.arguments.get(argument)
        if options != None:
            obj.add_argument(argument, **options)

    @classmethod
    def add_arguments(cls, obj, *arguments):
        """Adds multiple arguments.

        Takes a parser or a group object and adds arguments
        to it with their options.

        Args:
            obj: A parser or a group object to which the arguments
                are to be added.
            arguments: The arguments to add.
        """
        for argument in arguments:
            ArgumentAdder.add_argument(obj, argument)
    
    @classmethod
    def add_auth(cls, parser):
        """Adds authentication arguments.

        Takes a parser oject and adds a group of authentication
        arguments to it. These authentication arguments are the
        user's credentials, namely the email address and the
        password.

        Args:
            parser: The parser to add the authentication 
                arguments to.
        """
        group = parser.add_argument_group('Credentials', 'The credentials of your APIMatic account.')
        ArgumentAdder.add_arguments(group, '--email', '--password')

    @classmethod
    def add_input(cls, parser):
        """Adds input arguments.

        Takes a parser oject and adds a mutually exclusive group 
        of input arguments to it. These mutually exclusive 
        arguments are the file and url arguments. The user is only
        allowed to provide one of these to the program.

        Args:
            parser: The parser to add the input 
                arguments to.
        """
        mgroup = parser.add_mutually_exclusive_group(required=True)
        ArgumentAdder.add_arguments(mgroup, '--url', '--file')

