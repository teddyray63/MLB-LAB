/** Case-insensitive lookup in export player-keyed maps. */
export function lookupPlayerMap<T>(
  map: Record<string, T> | undefined,
  playerName: string | null | undefined,
): T | undefined {
  if (!map || !playerName) return undefined
  if (map[playerName]) return map[playerName]
  const key = Object.keys(map).find((k) => k.toLowerCase() === playerName.toLowerCase())
  return key ? map[key] : undefined
}
