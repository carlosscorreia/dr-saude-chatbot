# Dr. Saúde

ChatBot de atendimento de uma clínica, feito em Python para a disciplina de Desenvolvimento de Sistemas Computacionais para Processamento e Registro de Dados (UNIFAN).

Pelo menu o paciente pode marcar e cancelar consultas, ver se o exame está pronto, conferir as consultas marcadas para o retorno e pegar o contato da recepção.

## Como rodar

No Windows, dê dois cliques em `Abrir Dr. Saude.bat`. O chatbot abre no terminal.

Pelo terminal também funciona:

```
python atv_fan_01.py
```

Se o comando `python` não for encontrado, use `py atv_fan_01.py`.

### Gerar um .exe

```
pip install pyinstaller
pyinstaller DrSaude.spec
```

O executável fica em `dist/DrSaude.exe`. Em computadores com Smart App Control ou Device Guard ativo, o Windows pode bloquear o .exe por não ter assinatura digital. Nesse caso, use o `.bat`.

## Área administrativa

Digitando `0110` no menu principal, a clínica entra na área administrativa. Lá é possível:

- ver todas as consultas e registrar as que já foram realizadas;
- cadastrar exames, gerando o protocolo do paciente;
- liberar o resultado de um exame.

O ciclo completo para testar: o paciente marca uma consulta, a área administrativa registra o atendimento e cadastra um exame, libera o resultado, e o paciente passa a conseguir consultar o exame (opção 2) e marcar o retorno (opção 3).

## Equipe

- Angelo Lisboa
- Carlos Eduardo Silva Correia
- João Pedro da Silva Oliveira

Professora: Nadja Soraya Torres Dias
