# Script de Transcrição de Áudio para Texto

Este script em Python utiliza o modelo de linguagem de inteligência artificial da OpenAI para transcrever áudio em texto. Ele faz uso da biblioteca MoviePy para manipulação de arquivos de áudio e da biblioteca Whisper para interagir com o modelo de IA da OpenAI.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `openai-whisper`
- `moviepy`

Você pode instalá-las via pip:


- `pip install -U openai-whisper`
- `pip install moviepy`

## Como Usar

1. Coloque seus arquivos de áudio em um diretório separado e coloque o caminho dele na variável `diretorioA`.
2. Execute o script Python fornecido.
3. Os arquivos de texto transcritos serão armazenados no caminho que estiver na variável `diretorioT`.

Certifique-se de ajustar o caminho do diretório conforme necessário no código Python.

## Aviso Legal

Certifique-se de seguir os termos de serviço da OpenAI ao usar este script para transcrição de áudio em texto.

## Observação

Esse código está pronto para ser usado direto no Colaboratory.  
Há apenas uma coisa deve ser ajustada em um notebook do Colaboratory recém criado ou ainda não ajustado: 
- `Ambiente de execução -> Alterar o tipo de ambiente de execução -> Acelerador de hardware -> T4 GPU -> Salvar.`
