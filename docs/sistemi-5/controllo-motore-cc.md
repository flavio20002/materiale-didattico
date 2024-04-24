# Controllo di un motore in corrente continua

In questo capitolo, andremo ad analizzare un esempio di controllo analogico per un motore a corrente continua che fa uso di una dinamo tachimetrica.

## Schema di principio

## Implementazione con amplificatori operazionali

# Dimensionamento del segnale di riferimento

Per poter impostare il segnale di riferimento, si suppone che la velocità angolare d'uscita debba essere regolata fra due valori, chiamati $\omega_{\text{min}}$ e $\omega_{\text{max}}$. La tensione $V_{\text{ref}}$ prelevata dal partitore con l'inseguitore di tensione, può essere calcolata con la formula:

$$ V_{\text{ref}} = \frac{E}{R_1+R_2+R_3} [(1-\gamma) R_1 + R_3] $$

dove $\gamma$ varia tra 0 e 1 e rappresenta la posizione del cursore della resistenza variabile.
Si possono quindi ricavare le tensioni massime e minime di riferimento per i due valori limite di $\gamma$:

$$ \begin{cases}
  V_{\text{ref}}^{\text{min}} =  \dfrac{E}{R_1+R_2+R_3}  (R_3) \\[10pt]
  V_{\text{ref}}^{\text{max}} =  \dfrac{E}{R_1+R_2+R_3}  (R_1 + R_3)
\end{cases}\, $$

Le resistenze devono essere scelte in modo che la corrente non sia troppo eccessiva e quindi dissipare potenza inutilmente e troppo ridotta, tale da essere sensibile a disturbi esterni. La corrente dovrebbe essere quindi nell'ordine di 1 mA.

## Amplificatore differenziale

L'amplificatore differenziale deve sottrarre dal segnale di riferimento il segnale proveniente dal trasduttore. È possibile dunque utilizzare una configurazione a guadagno unitario in cui tutte le resistenza sono uguali e possono essere scelte nell'ordine di 1 k$\Omega$.

## S

