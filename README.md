# 🧠 Tutorial de Instalação do SimPy em Linux Debian 13 (Trixie)

## 🧩 1. O que é o SimPy

**SimPy** é uma biblioteca de **simulação de eventos discretos** em Python.  
Permite modelar filas, processos e sistemas complexos de forma elegante e baseada em processos.

📦 Documentação oficial: [https://simpy.readthedocs.io/](https://simpy.readthedocs.io/)  
PyPI: [https://pypi.org/project/simpy/](https://pypi.org/project/simpy/)

---

## ⚙️ 2. Verificando o ambiente

Antes de instalar o SimPy, verifique se o Python 3 e o `pip` estão disponíveis:

```bash
python3 --version
pip3 --version
```

Se não estiverem instalados:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

---

## 🧱 3. Criando um ambiente virtual (recomendado)

```bash
mkdir ~/projetos_simpy
cd ~/projetos_simpy
python3 -m venv venv
source venv/bin/activate
```

Verifique se o ambiente está ativo (aparecerá `(venv)` no prompt).

---

## 🧰 4. Instalando o SimPy

```bash
pip install simpy
```

Para verificar:

```bash
python3 -c "import simpy; print(simpy.__version__)"
```

---

## 🧪 5. Teste rápido

Crie um arquivo `teste_simpy.py`:

```python
import simpy

def processo(env):
    while True:
        print(f"Tempo atual: {env.now}")
        yield env.timeout(1)

env = simpy.Environment()
env.process(processo(env))
env.run(until=5)
```

Execute:

```bash
python3 teste_simpy.py
```

Saída esperada:

```
Tempo atual: 0
Tempo atual: 1
Tempo atual: 2
Tempo atual: 3
Tempo atual: 4
```

---

## 🧩 6. Pacotes adicionais (opcional)

Instale ferramentas úteis para análise e visualização:

```bash
pip install matplotlib pandas numpy
```

Esses pacotes auxiliam em:
- Visualização de resultados (`matplotlib`)
- Armazenamento de dados (`pandas`)
- Estatísticas e distribuições (`numpy`)

---

## 🧹 7. Atualizar ou remover

Atualizar:

```bash
pip install --upgrade simpy
```

Remover:

```bash
pip uninstall simpy
```

---

## 🧠 8. Dicas para Debian/Linux

- Se usar VS Code:  
  `Ctrl + Shift + P` → *Python: Select Interpreter* → escolha `venv/bin/python`

- Listar pacotes:
  ```bash
  pip list
  ```

- Exportar dependências:
  ```bash
  pip freeze > requirements.txt
  ```

---

## ✅ Resumo rápido

| Etapa | Comando |
|-------|----------|
| Atualizar pacotes | `sudo apt update` |
| Instalar Python e pip | `sudo apt install python3 python3-pip python3-venv` |
| Criar ambiente virtual | `python3 -m venv venv` |
| Ativar ambiente | `source venv/bin/activate` |
| Instalar SimPy | `pip install simpy` |
| Testar instalação | `python3 -c "import simpy; print(simpy.__version__)"` |

---

## 🐳 Instalação via Docker (opcional)

Se preferir um ambiente totalmente isolado:

**Crie um arquivo `Dockerfile`:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir simpy matplotlib pandas numpy

CMD ["python3"]
```

**Para construir e executar:**

```bash
docker build -t simpy-env .
docker run -it simpy-env
```

---
