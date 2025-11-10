make setup        # create venv, install deps, pre-commit
make eda          # open notebook
make train        # train with configs/baseline.yaml
make eval         # evaluate and write report to /src/data/metrics.json
make api          # start FastAPI locally
make test         # run unit/integration tests
make docker       # build image