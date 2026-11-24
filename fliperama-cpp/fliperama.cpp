/*
* Disciplina: 2026-PCAP
* Projeto   : MeuApp v4.0 - o Fliperama em C++ (Aula 32)
* Autor     : Maria Eduarda Denck
* LIAC      : Menu com validacao, cadastro de jogadores em dois vectors que crescem , um jogo que conta partidas por jogador e o cadastro salvo em arquivo na saída e relido na entrada.
*/


#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define DONO "MARIAA"

void linha() {
    cout << "===========================" << endl;
}

void titulo(string texto) {
    linha();
    cout << " " << texto << endl;
    linha();
}

int ler_numero(string mensagem, int minimo, int maximo) {
    int numero;

    cout << mensagem << ": ";
    cin >> numero;
    while (cin.fail() || numero < minimo || numero > maximo) {
        if (cin.fail()) {
            cin.clear();
            cin.ignore(1000, '\n');
        }
        cout << "Opcao invalida! Tente de novo: ";
        cin >> numero;
    }
    return numero;
}

string ler_texto(string mensagem) {
    string texto;

    cout << mensagem << ": ";
    cin >> texto;
    return texto;
}

void cadastrar(vector<string> apelidos, vector<int> partidas) {
    string novo;

    titulo("NOVO JOGADOR");
    novo = ler_texto("Apelido (sem espacos)");

    apelidos.push_back(novo);
    partidas.push_back(0);
    cout << "Jogador " << novo << " cadastrado." << endl;
}

void listar(vector<string> &apelidos, vector<int> &partidas) {
    int i, qtd = apelidos.size();

    titulo("JOGADORES CADASTRADOS");
    if (qtd == 0) {
        cout << "Nenhum jogador cadastrado ainda." << endl;
    }
    for (i = 0; i < qtd; i++) {
        cout << apelidos[i] << " | " << partidas[i] << " partidas" << endl;
    }
}

void mostrar_menu() {
    linha();
    cout << "  FLIPERAMA DO " << DONO << endl;
    linha();
    cout << "[1] Adivinhe o Numero" << endl;
    cout << "[2] Cadastrar Jogador" << endl;
    cout << "[3] Listar Jogadores" << endl;
    cout << "[0] Sair" << endl;
    linha();
}

int main() {
    vector<string> apelidos;
    vector<int> partidas;
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0) {
        if (opcao == 1) {
            cout << "O jogo entra na fase 3." << endl;
        } else if (opcao == 2) {
            cadastrar(apelidos, partidas);
             cout << "O jogo entra na fase 2." << endl;
        } else {
            listar(apelidos, partidas);
             cout << "O cadastro entra na fase 2." << endl;
        } 
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }

    titulo("Ate a proxima!");
    return 0;
}