// Pregunta 3: Carrera de liebres
function carrera(posA, velA, posB, velB) {
    // Si ambas liebres empiezan en la misma posición
    if (posA === posB) return `Ambas liebres ya están en el mismo cuadrante: ${posA}.`;

    // Si las liebres tienen la misma velocidad pero empiezan en posiciones diferentes, nunca se encontrarán
    if (velA === velB) return "Las liebres nunca se encontrarán en el mismo cuadrante.";

    // Comprobamos si el cruce es posible
    const diferenciaPos = posB - posA;
    const diferenciaVel = velA - velB;

    if (diferenciaPos % diferenciaVel === 0) {
        const puntoDeEncuentro = posA + (diferenciaPos / diferenciaVel) * velA;
        return `Las liebres se encontrarán en el cuadrante ${puntoDeEncuentro}.`;
    }

    return "Las liebres nunca se encontrarán en el mismo cuadrante.";
}

// Ejemplo de uso
console.log(carrera(0, 3, 4, 2));  // Imprimirá algo como: "Las liebres se encontrarán en el cuadrante 12."



