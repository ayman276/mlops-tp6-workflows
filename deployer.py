from pathlib import Path
from flow_mlops import reentrainement

if __name__ == '__main__':
    # source = le dossier local du projet : le worker execute le code ici,
    # la ou se trouvent les donnees DVC (pas de git clone)
    reentrainement.from_source(
        source=str(Path(__file__).parent.resolve()),
        entrypoint='flow_mlops.py:reentrainement',
    ).deploy(
        name='hebdomadaire-pool',
        work_pool_name='pool-tp',
        cron='0 6 * * 1',
    )