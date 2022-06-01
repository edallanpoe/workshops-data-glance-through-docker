import __meta__ as meta
import src.utils.parameters as args
from src.utils.exceptions import BadConfigValidatorError
from src.demo.general import AnalyzeGpx
from src.demo.report import GeneratePdf


class App:

    if __name__ == "__main__":
        app = None
        app = meta.get_app_instances()
        app.args = args.get_args().parse_args()

        if app.logger is not None:
            try:
                if app.args.command == 'run-process':
                    analyzeGpx = AnalyzeGpx(app)
                    analyzeGpx.start()
                elif app.args.command == 'generate-report':
                    generatePdf = GeneratePdf(app)
                    generatePdf.start()
            except Exception as ex:
                app.logger.error(str(ex))
                exit(1)
        else:
            raise BadConfigValidatorError("config is bad configured, check please.")
