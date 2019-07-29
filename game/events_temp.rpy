init offset -2 python:

    # Отработанные события:

    worked_event = []

    # События:

    good_usual_events = [
        {
            "text": "В Альбис приехали артисты",
            "influence": {
                "event": "albis_artists"
            }
        },

        {
            "text": "В Хестир приехали артисты",
            "influence": {
                "event": "hestir_artists"
            }
        },

        {
            "text": "В Нокс приехали артисты",
            "influence": {
                "event": "nox_artists"
            }
        },

        {
            "text": "В Виллалдан приехали артисты",
            "influence": {
                "event": "willaldan_artists"
            }
        },

        {
            "text": "В Осталикон приехали артисты",
            "influence": {
                "event": "hostalikon_artists"
            }
        },

        {
            "text": "В Галеренон приехали артисты",
            "influence": {
                "event": "galerenon_artists"
            }
        },

        {
            "text": "Выставка народного хозяйства в Альбисе",
            "influence": {
                "event": "albis_nat_econ_exhib"
            }
        },

        {
            "text": "Выставка народного хозяйства в Хестире",
            "influence": {
                "event": "hestir_nat_econ_exhib"
            }
        },

        {
            "text": "Выставка народного хозяйства в Ноксе",
            "influence": {
                "event": "noks_nat_econ_exhib"
            }
        },

        {
            "text": "Выставка народного хозяйства в Виллалдане",
            "influence": {
                "event": "willaldan_nat_econ_exhib"
            }
        },

        {
            "text": "Выставка народного хозяйства в Осталиконе",
            "influence": {
                "event": "hostalikon_nat_econ_exhib"
            }
        },

        {
            "text": "Выставка народного хозяйства в Галереноне",
            "influence": {
                "event": "galerenon_nat_econ_exhib"
            }
        },

        {
            "text": "Появление рок-музыки",
            "influence": {
                "event": "rock_music"
            }
        },
    ]

    good_rare_events = [
        {
            "text": "Изобретено лекарство от Алеанис Фунгуса"
            "influence": {
                "event": "fungus_medicine",
            }
        }

        {
            "text": "В деревне А не поделили сено для скота. Выжило только три семьи",
            "influence": {
                "event": "a_country_skirmish"
            }
        },

        {
            "text": "В Альбис приехала большая ярмарка",
            "influence": {
                "event": "albis_fair"
            }
        },

        {
            "text": "В Хестир приехала большая ярмарка",
            "influence": {
                "event": "hestir_fair"
            }
        },

        {
            "text": "В Нокс приехала большая ярмарка",
            "influence": {
                "event": "noks_fair"
            }
        },

        {
            "text": "В Виллалдан приехала большая ярмарка",
            "influence": {
                "event": "willaldan_fair"
            }
        },

        {
            "text": "В Осталикон приехала большая ярмарка",
            "influence": {
                "event": "hostalikon_fair"
            }
        },

        {
            "text": "В Галеренон приехала большая ярмарка",
            "influence": {
                "event": "galerenon_fair"
            }
        },
    ]

    good_urare_events = [
        {
            "text": "Выставка научных достижений в Альбисе"
            "influence": {
                "event": "albis_sci_exhib"
            }
        },
    ]

    bad_usual_events = [
        {
            "text": "В Осталиконе произошла вспышка бешенства диких животных",
            "influence": {
                "event": "ostalikon_rabies_wild"
            }
        }
    ]
