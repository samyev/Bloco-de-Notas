from main import BlocoNotas

# Gerando as janelas de interação do bloconotas
if __name__ == "__main__":
    #metodos OBRIGATORIOS para inicializar o banco
    notasClass = BlocoNotas("bloconotas.db", "notes")
    notasClass.createDatabaseSchema()

    # Menu do Bloco de Notas
    print("----------Bloco de Notas----------")
    inputValue = int(input("""
    Escolha uma opção:
    1 - Criar nota
    2 - Visualizar nota
    3 - Editar texto de uma nota
    4 - Editar tags de uma nota
    5 - Deletar uma nota
    """))
    
    # Chamando função createNote para criar as notas
    if inputValue == 1:
        noteText = input("Digite o texto da nota: \n")
        print("(ex: tag1, frase)")
        tagText = input("Digite as tags da nota (a nota pode ter tags vazias): ")
        notasClass.createNote(noteText, tagText)
    # Chamando função searchNotes para buscar as notas pelas tags
    elif inputValue == 2:
        optSearch = input("Digite a tag que deseja visualizar as notas(vazio vai mostrar todas as notas):")
        if optSearch == "":
            notasClass.searchNotes()
        else:
            notasClass.searchNotes(optSearch)
    # chamando função modifyNote para modificar o texto da nota desejada
    elif inputValue == 3:
        idNote = int(input("Digite o id da nota que quer modificar: "))
        if notasClass.searchNotesByID(idNote):
            noteText = input("Digite o novo texto da nota: ")
            notasClass.modifyNote(idNote,noteText)
        else:
            print (f"A nota com o Id {idNote} não existe, tente novamente!")
    # Chamando a função modifyNote para modificar uma tag
    elif inputValue == 4:
        idNote = int(input("Digite o id da nota que quer modificar: "))
        if notasClass.searchNotesByID(idNote):
            tagNote = input("Digite as tags da nota (separado pro virgula): ")
            notasClass.modifyNote(idNote,"", tagNote)
        else:
            print (f"A nota com o Id {idNote} não existe, tente novamente!")
    # Chamando função deleteNote para deletar uma nota
    elif inputValue == 5:
        idNote = int(input("Digite o id da nota que você deseja deletar: "))
        if notasClass.searchNotesByID(idNote):
            notasClass.deleteNote(idNote)
    # Mostrando que alguma opção que você digitou é invalida
    else:
        print("Opção invalida, tente novamente!")
        exit()
