
APP=${PWD}

source $APP/components/bash/utilities.sh

function stage_0(){
    path_resutls=$1
    clear
    echo "    _____ _______ ______ _____      _  _      ___  "
    echo "   / ____|__   __|  ____|  __ \   _| || |_   / _ \ "
    echo "  | (___    | |  | |__  | |__) | |_  __  _| | | | |"
    echo "   \___ \   | |  |  __| |  ___/   _| || |_  | | | |"
    echo "   ____) |  | |  | |____| |      |_  __  _| | |_| |"
    echo "  |_____/   |_|  |______|_|        |_||_|    \___/ "
    echo ""
    tree $path_resutls
}                                                
           
function stage_1(){
    clear
    echo "   _____ _______ ______ _____      _  _     __ "
    echo "  / ____|__   __|  ____|  __ \   _| || |_  /_ |"
    echo " | (___    | |  | |__  | |__) | |_  __  _|  | |"
    echo "  \___ \   | |  |  __| |  ___/   _| || |_   | |"
    echo "  ____) |  | |  | |____| |      |_  __  _|  | |"
    echo " |_____/   |_|  |______|_|        |_||_|    |_|"
    echo ""
    echo " read code validation"
    echo "  ├── clean temporary files"
    echo "  ├── mypy validations"
    echo "  ├── flake8 validations"
    echo "  ├── remove validations temp file"
    echo "  └── clean outpus"
    echo ""
}

function stage_2(){
    clear
    echo "   _____ _______ ______ _____      _  _     ___  "
    echo "  / ____|__   __|  ____|  __ \   _| || |_  |__ \ "
    echo " | (___    | |  | |__  | |__) | |_  __  _|    ) |"
    echo "  \___ \   | |  |  __| |  ___/   _| || |_    / / "
    echo "  ____) |  | |  | |____| |      |_  __  _|  / /_ "
    echo " |_____/   |_|  |______|_|        |_||_|   |____|"
    echo ""
    echo " processing gps files"
    echo " ├── python.read.gpx          ├── python.geopandas.maps"
    echo " │   ├── get fields           │   ├── get fields"
    echo " │   │   ├── latitude         │   │   ├── add map (cities)"
    echo " │   │   ├── longitude        │   │   ├── add map (city roads)"
    echo " │   │   └── date             │   │   └── generate maps"
    echo " ├── python.pandas.etl        ├── spark.processing.elt"
    echo " │   ├── set fields           │   ├── compressed data"
    echo " │   │   ├── event_date       │   ├── consolidate data"
    echo " │   │   ├── start_latitude   └── └── read parametric"
    echo " │   │   ├── start_longitude "
    echo " │   │   ├── elevation "
    echo " │   │   ├── end_latitude "
    echo " │   │   ├── end_longitude"
    echo " │   │   ├── distance "
    echo " │   │   ├── tag "
    echo " │   │   ├── event_mark_time "
    echo " │   │   ├── event_year"
    echo " │   │   ├── event_month"
    echo " │   │   ├── event_day"
    echo " │   │   ├── event_hour"
    echo " │   │   ├── event_minute"
    echo " │   │   ├── event_second"
    echo " │   │   ├── vehicle_type"
    echo " └── └── └── vehicle_id"                                                                                          
}

function stage_3(){
    clear
    echo "    _____ _______ ______ _____      _  _     ____  "
    echo "   / ____|__   __|  ____|  __ \   _| || |_  |___ \ "
    echo "  | (___    | |  | |__  | |__) | |_  __  _|   __) |"
    echo "   \___ \   | |  |  __| |  ___/   _| || |_   |__ < "
    echo "   ____) |  | |  | |____| |      |_  __  _|  ___) |"
    echo "  |_____/   |_|  |______|_|        |_||_|   |____/ "
    echo ""
    echo "  python.generate.report"  
    echo "  ├── analyze images"
    echo "  ├── set up variables"
    echo "  ├── calculate dynamic rows and columns"
    echo "  ├── merge images"
    echo "  ├── generate plot"
    echo "  └── generate pdf"
    echo ""                                          
                                                  
}

function stage_4(){
    clear
    echo "   _____ _______ ______ _____      _  _     _  _   "   
    echo "  / ____|__   __|  ____|  __ \   _| || |_  | || |  "
    echo " | (___    | |  | |__  | |__) | |_  __  _| | || |_ "
    echo "  \___ \   | |  |  __| |  ___/   _| || |_  |__   _|"
    echo "  ____) |  | |  | |____| |      |_  __  _|    | |  "
    echo " |_____/   |_|  |______|_|        |_||_|      |_|  "
    echo ""
    echo " spark.web.console"
    echo "  ├── explore jupyter notebook"
    echo "  ├── explore spark web"
    echo "  ├── analyze code"
    echo "  ├── analyze pdf generated"
    echo "  ├── explanation spark code"
    echo "  ├── analyzing spark job"
    echo "  └── recomendations"
    echo "" 
    echo "please open in your browser"
    echo ""
    echo "      jupyter notebook ----> http://localhost:8000/workshop/"
    echo "      spark history    ----> http://localhost:4040/"
    echo "      pdf              ----> $(pwd)/data/output/results/pdf"
    echo "                       └───> $(pwd)/results/pdf"
    echo ""
}                                           
                                                   

function demo_welcome(){                                                                                                                                                        
    echo_color $CONST_COLOR_BLUE  "                                   .!!!:                       .::.::.      "
    echo_color $CONST_COLOR_BLUE  "                                   ~&&&?                       .??:J        " 
    echo_color $CONST_COLOR_BLUE  "                                  ^#&&?                       ~J: 7J.       "	
    echo_color $CONST_COLOR_BLUE  "   :!JY5555J !55Y:          :Y5YY5YP##&GY555555555555555Y?!.   :  :.        "
    echo_color $CONST_COLOR_BLUE  "  ?#&&&####G J&&&~          ^#&&&#######################&&&B~               "
    echo_color $CONST_COLOR_BLUE  " ^#&&P^::::. J&&#^          :B&&5:.!##&J.:::::::::::::::~B&&G.              "
    echo_color $CONST_COLOR_BLUE  " ~&#&?       J&&#^          :B&&Y  ~#&&?                 5&&B:              "
    echo_color $CONST_COLOR_BLUE  " ~&#&?       J&&#^          :B&&Y  ~#&&?   ^?YPPPPPPPPPPP#&##GPPPPPPPPPPG5!."
    echo_color $CONST_COLOR_BLUE  " ~&#&?       J&&#^          :B&&Y  ~#&&?  J#&&#BBBBBBBBBB####BBBBBBBBBBGJ:  "
    echo_color $CONST_COLOR_BLUE  " ~&#&?       J&&#^          :B&&Y  ~#&&? ^#&&5:......... 5&&B^ ........     "
    echo_color $CONST_COLOR_BLUE  " ~&#&?       ?&&&?.        .7#&&Y  ~#&&? ^#&&5.         ^G&&B.              "
    echo_color $CONST_COLOR_BLUE  " ~&&&?       :P&&&BGGGGGGGGB&&&G^  ~&&&?  J&&&#BGGGGGGGB#&&#7               "
    echo_color $CONST_COLOR_BLUE  " ^GPG!        .!J5PGGGGGGGGP5Y!.   ^PPG7   ^?5PGGGGGGGGGPY?:                "                                                                       
}

function sep_step(){
	echo ""
	echo "-------------------------------------------------------------------------------"
	echo ""
}


function demo_body(){
echo "        _..._           o               .        ___---___                    .          "         
echo "      .'     '.      _         .              .--\        --.     .     .         .      "
echo "     /    .-""-\   _/ \                     ./.;_.\     __/~ \.                          "
echo "   .-|   /:.   |  |   |                    /;  /  -   __\    . \                         "                       
echo "   |  \  |:.   /.- -./   .        .       /  --      / .   .;   \        |               "
echo "   | .- -;:__.     =/                    | .|       /       __   |      -O-              "
echo "   .'=  *=|NASA _.='                    |__/    __ |  . ;   \ | . |      |               "
echo "  /   _.  |    ;                        |      /  \\_    . ;| \___|                      "
echo " ;-.- |    \   |           .    o       |      \  .~\\___ --      |           .          "
echo "/   | \    _\  _\                        |     | . ; ~~~~\_    __|                       "
echo "\__/ ._;.  ==' ==\          |             \    \   .  .  ; \  /_/   .                    "
echo "         \    \   |        -O-        .    \   /         . |  ~/                  .      "
echo "         /    /   /         |    .          ~\ \   .      /  /~          o               "
echo "         /-._/-._/        .                   ~--___ ; ___--~                            "
echo "         \    \  \                       .          ---         .                        "  
echo "           -._/._/                                                                       "
echo ""
}